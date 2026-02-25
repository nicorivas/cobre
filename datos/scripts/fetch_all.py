#!/usr/bin/env python3
"""
Orquestador: corre todos los fetchers en orden y produce un resumen.

Uso:
    python datos/scripts/fetch_all.py                # datos recientes (30 días)
    python datos/scripts/fetch_all.py --days 365     # último año
    python datos/scripts/fetch_all.py --backfill     # backfill completo (2 años precios, 3 años COT)
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

# Cargar .env antes de lanzar subprocesos para que hereden las variables
from dotenv import load_dotenv
SCRIPTS_DIR = Path(__file__).resolve().parent
DATOS_DIR = SCRIPTS_DIR.parent
load_dotenv(DATOS_DIR / ".env")
load_dotenv(DATOS_DIR.parent / ".env")

PYTHON = sys.executable


def run_script(name: str, args: list[str] | None = None, optional_env: dict | None = None):
    """Ejecuta un script de fetch. Imprime output en tiempo real."""
    script = SCRIPTS_DIR / name
    cmd = [PYTHON, str(script)] + (args or [])
    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"{'='*60}\n")
    result = subprocess.run(cmd, env={**__import__("os").environ, **(optional_env or {})})
    if result.returncode != 0:
        print(f"\n  ADVERTENCIA: {name} terminó con código {result.returncode}")
    return result.returncode


def main():
    parser = argparse.ArgumentParser(description="Run all data fetchers")
    parser.add_argument("--days", type=int, default=30, help="Días hacia atrás para precios (default: 30)")
    parser.add_argument("--backfill", action="store_true", help="Backfill extendido")
    args = parser.parse_args()

    if args.backfill:
        price_days = 730
        cot_backfill = 3
    else:
        price_days = args.days
        cot_backfill = 1

    # 1. Inicializar DB si no existe
    db_path = SCRIPTS_DIR.parent / "cobre.duckdb"
    if not db_path.exists():
        print("Base de datos no encontrada. Inicializando...")
        run_script("init_db.py")

    results = {}

    # 2. Precios de mercado (yfinance — no requiere API key)
    results["comex"] = run_script("fetch_comex.py", [f"--days={price_days}"])

    # 3. FRED macro (requiere FRED_API_KEY en datos/.env)
    if os.environ.get("FRED_API_KEY"):
        results["fred"] = run_script("fetch_fred.py", [f"--days={price_days}"])
    else:
        print(f"\n{'='*60}")
        print(f"  fetch_fred.py — SALTADO (FRED_API_KEY no definida)")
        print(f"{'='*60}")
        results["fred"] = "skipped"

    # 4. LME (Westmetall — no requiere API key)
    lme_args = [f"--years={max(2, price_days // 365 + 1)}"] if args.backfill else ["--years=2"]
    results["lme"] = run_script("fetch_lme.py", lme_args)

    # 5. CFTC COT
    results["cot"] = run_script("fetch_cot.py", [f"--backfill={cot_backfill}"])

    # 6. SHFE (lento desde fuera de China — timeout de 60s por request)
    shfe_args = [f"--days={price_days}"]
    results["shfe"] = run_script("fetch_shfe.py", shfe_args)

    # 7. Spreads calculados (depende de COMEX + LME + SHFE, correr al final)
    results["spreads"] = run_script("calc_spreads.py")

    # Resumen final
    print(f"\n{'='*60}")
    print(f"  RESUMEN")
    print(f"{'='*60}\n")
    for script, rc in results.items():
        status = "OK" if rc == 0 else ("SALTADO" if rc == "skipped" else f"ERROR ({rc})")
        print(f"  {script:12s} → {status}")

    # Estado de la DB
    sys.path.insert(0, str(SCRIPTS_DIR))
    from db import query
    print(f"\nSeries en clean.prices:")
    try:
        print(query("SELECT series_id, min(trade_date) AS desde, max(trade_date) AS hasta, count(*) AS n FROM clean.prices GROUP BY series_id ORDER BY series_id").to_string(index=False))
    except Exception:
        pass

    print(f"\nCOT en clean.cot:")
    try:
        print(query("SELECT min(report_date) AS desde, max(report_date) AS hasta, count(*) AS semanas FROM clean.cot").to_string(index=False))
    except Exception:
        pass


if __name__ == "__main__":
    main()
