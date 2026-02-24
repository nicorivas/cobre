#!/usr/bin/env python3
"""
Descarga indicadores macro desde FRED (Federal Reserve Economic Data).

Series: Fed Funds Rate, ISM Manufacturing PMI.

Requiere: FRED_API_KEY en datos/.env (se carga automáticamente via db.py).
  Obtener gratis en: https://fred.stlouisfed.org/docs/api/api_key.html

Uso:
    python datos/scripts/fetch_fred.py              # últimos 2 años
    python datos/scripts/fetch_fred.py --days 365   # último año
"""

import argparse
import os
import sys
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from db import connect, ingest_raw, upsert_prices, upsert_macro, DB_PATH

FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"

# Mapeo de series FRED → nuestro schema
SERIES = {
    "DFF": {
        "series_id": "fed_funds",
        "unit": "pct",
        "target": "macro",
        "name": "Fed Funds Rate",
    },
    "INDPRO": {
        "series_id": "indpro",
        "unit": "index",
        "target": "macro",
        "name": "Industrial Production Index",
    },
    "DTWEXBGS": {
        "series_id": "dxy_fred",
        "unit": "index",
        "target": "prices",
        "name": "Trade Weighted USD (broad)",
    },
}


def fetch_fred_series(
    fred_id: str, api_key: str, start: date, end: date
) -> pd.DataFrame:
    """Descarga una serie de FRED y retorna DataFrame."""
    params = {
        "series_id": fred_id,
        "api_key": api_key,
        "file_type": "json",
        "observation_start": str(start),
        "observation_end": str(end),
    }
    resp = requests.get(FRED_BASE, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    if "observations" not in data:
        return pd.DataFrame()

    rows = []
    for obs in data["observations"]:
        if obs["value"] == ".":  # FRED usa "." para missing
            continue
        rows.append({
            "obs_date": obs["date"],
            "value": float(obs["value"]),
        })

    df = pd.DataFrame(rows)
    if not df.empty:
        df["obs_date"] = pd.to_datetime(df["obs_date"]).dt.date
    return df


def main():
    parser = argparse.ArgumentParser(description="Fetch macro data from FRED API")
    parser.add_argument("--days", type=int, default=730, help="Días hacia atrás (default: 730)")
    parser.add_argument("--start", type=str, help="Fecha inicio (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, help="Fecha fin (YYYY-MM-DD)")
    args = parser.parse_args()

    api_key = os.environ.get("FRED_API_KEY")
    if not api_key:
        print("ERROR: Variable de entorno FRED_API_KEY no definida.")
        print("Obtener gratis en: https://fred.stlouisfed.org/docs/api/api_key.html")
        sys.exit(1)

    if args.start:
        start = date.fromisoformat(args.start)
        end = date.fromisoformat(args.end) if args.end else date.today()
    else:
        end = date.today()
        start = end - timedelta(days=args.days)

    con = connect(DB_PATH)
    total_rows = 0

    for fred_id, meta in SERIES.items():
        print(f"Descargando {meta['name']} ({fred_id})...")
        try:
            df = fetch_fred_series(fred_id, api_key, start, end)
        except Exception as e:
            print(f"  ERROR: {e}")
            continue

        if df.empty:
            print(f"  Sin datos.")
            continue

        print(f"  {len(df)} observaciones")

        # Raw
        raw_df = df.copy()
        raw_df["series_id"] = meta["series_id"]
        raw_df["trade_date"] = raw_df["obs_date"]
        raw_df["unit"] = meta["unit"]
        ingest_raw(con, source="fred", df=raw_df)

        # Clean
        if meta["target"] == "macro":
            macro_df = df.copy()
            macro_df["series_id"] = meta["series_id"]
            upsert_macro(con, macro_df)
            print(f"  → clean.macro")
        elif meta["target"] == "prices":
            prices_df = df.rename(columns={"obs_date": "trade_date", "value": "close"}).copy()
            prices_df["series_id"] = meta["series_id"]
            prices_df["unit"] = meta["unit"]
            upsert_prices(con, prices_df)
            print(f"  → clean.prices")

        total_rows += len(df)

    print(f"\nTotal: {total_rows} observaciones ingestadas.")
    con.close()


if __name__ == "__main__":
    main()
