#!/usr/bin/env python3
"""
Descarga precios, inventarios y posicionamiento de SHFE Copper.

Fuente: shfe.com.cn — endpoints JSON/HTML públicos, sin API key.
Nota: SHFE puede ser lento desde fuera de China (timeout de 60s).

Series:
  - shfe_cu: precio settlement del contrato más activo (RMB/ton)
  - shfe inventories: stocks totales de cobre en warehouses SHFE
  - shfe_cu_top20_net: top 20 miembros long - short (posicionamiento)

Uso:
    python datos/scripts/fetch_shfe.py              # últimos 30 días
    python datos/scripts/fetch_shfe.py --days 365   # último año
"""

import argparse
import sys
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).resolve().parent))
from db import connect, ingest_raw, upsert_prices, upsert_inventories, upsert_spreads, DB_PATH

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}
TIMEOUT = 60  # SHFE es lento desde fuera de China

# URL del endpoint de precios diarios (JSON).
# SHFE cambió la URL en jul-2025. Este es el patrón actual.
DAILY_URL = "https://www.shfe.com.cn/data/tradedata/future/dailydata/kx{date}.dat"

# URL del endpoint de posicionamiento top 20 (JSON)
RANK_URL = "https://www.shfe.com.cn/data/tradedata/future/dailydata/pm{date}.dat"

# URL del endpoint de inventarios (HTML).
# Cambió en nov-2025; este es el patrón actual.
STOCK_URL = "https://www.shfe.com.cn/data/tradedata/future/stockdata/dailystock_{date}/ZH/all.html"
# Patrón anterior (funciona hasta 2025-11-17)
STOCK_URL_OLD = "https://www.shfe.com.cn/data/tradedata/future/dailydata/{date}dailystock.dat"

# Fecha de corte entre endpoints de inventarios
STOCK_URL_CUTOVER = date(2025, 11, 18)


def _get_json(url: str) -> dict | None:
    """GET request que retorna JSON o None si falla."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if r.status_code == 404:
            return None
        r.raise_for_status()
        return r.json()
    except requests.exceptions.Timeout:
        return None
    except Exception:
        return None


def _trading_dates(start: date, end: date) -> list[date]:
    """Genera fechas de lunes a viernes entre start y end."""
    dates = []
    d = start
    while d <= end:
        if d.weekday() < 5:  # lun-vie
            dates.append(d)
        d += timedelta(days=1)
    return dates


def fetch_daily_prices(start: date, end: date) -> pd.DataFrame:
    """
    Descarga precios diarios SHFE copper.
    Selecciona el contrato con mayor OI como front month.
    """
    rows = []
    dates = _trading_dates(start, end)
    print(f"Descargando precios SHFE: {len(dates)} fechas ({start} → {end})")

    for d in dates:
        date_str = d.strftime("%Y%m%d")
        data = _get_json(DAILY_URL.format(date=date_str))
        if data is None:
            continue

        instruments = data.get("o_curinstrument", [])
        cu = [
            rec for rec in instruments
            if str(rec.get("PRODUCTGROUPID", "")).strip() == "cu"
            and str(rec.get("DELIVERYMONTH", "")).strip() != ""
            # Excluir fila de subtotales
            and "小计" not in str(rec.get("DELIVERYMONTH", ""))
        ]

        if not cu:
            continue

        # Front month = contrato con mayor OI
        try:
            front = max(cu, key=lambda x: int(x.get("OPENINTEREST", 0) or 0))
        except (ValueError, TypeError):
            continue

        settle = front.get("SETTLEMENTPRICE")
        close = front.get("CLOSEPRICE")
        high = front.get("HIGHESTPRICE")
        low = front.get("LOWESTPRICE")
        volume = front.get("VOLUME")
        oi = front.get("OPENINTEREST")

        if settle is None and close is None:
            continue

        price = settle if settle else close

        # Calcular OI total de cobre (suma de todos los contratos)
        total_oi = sum(int(c.get("OPENINTEREST", 0) or 0) for c in cu)

        rows.append({
            "trade_date": d,
            "series_id": "shfe_cu",
            "close": float(price),
            "high": float(high) if high else None,
            "low": float(low) if low else None,
            "volume": float(volume) if volume else None,
            "unit": "cny_per_ton",
            "oi": total_oi,
            "front_month": str(front.get("DELIVERYMONTH", "")).strip(),
        })

    df = pd.DataFrame(rows)
    if not df.empty:
        print(f"  {len(df)} días de precios obtenidos")
        print(f"  Último: {df.iloc[-1]['trade_date']} cu{df.iloc[-1]['front_month']} = {df.iloc[-1]['close']:.0f} RMB/t")
    else:
        print("  Sin datos de precios")
    return df


def fetch_inventories(start: date, end: date) -> pd.DataFrame:
    """
    Descarga inventarios SHFE copper (total warehouses).
    Usa el endpoint HTML nuevo (post nov-2025) o el JSON antiguo.
    """
    rows = []
    dates = _trading_dates(start, end)
    # Inventarios solo se publican ciertos días (no todos los trading days)
    # Intentamos todos y aceptamos los que respondan.
    print(f"Descargando inventarios SHFE: probando {len(dates)} fechas")

    for d in dates:
        date_str = d.strftime("%Y%m%d")

        if d >= STOCK_URL_CUTOVER:
            total = _fetch_stock_html(date_str)
        else:
            total = _fetch_stock_json(date_str)

        if total is not None:
            rows.append({
                "trade_date": d,
                "exchange": "shfe",
                "category": "total",
                "volume_mt": float(total),
            })

    df = pd.DataFrame(rows)
    if not df.empty:
        print(f"  {len(df)} días de inventarios obtenidos")
        print(f"  Último: {df.iloc[-1]['trade_date']} = {df.iloc[-1]['volume_mt']:.0f} t")
    else:
        print("  Sin datos de inventarios")
    return df


def _fetch_stock_html(date_str: str) -> float | None:
    """Parse inventarios desde endpoint HTML (post nov-2025)."""
    url = STOCK_URL.format(date=date_str)
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if r.status_code != 200:
            return None
        soup = BeautifulSoup(r.text, "html.parser")
        tables = soup.find_all("table", class_="el-table_table")
        if not tables:
            return None

        # La primera tabla es cobre. Buscar la última fila "合计" (total general).
        table = tables[0]
        totals = []
        for tr in table.find_all("tr"):
            cells = [td.get_text(strip=True) for td in tr.find_all("td")]
            if any("合计" in c for c in cells):
                # El valor de stock está en la penúltima celda numérica
                for c in cells:
                    c_clean = c.replace(",", "").strip()
                    try:
                        totals.append(float(c_clean))
                    except ValueError:
                        pass

        if not totals:
            return None

        # La primera fila "合计" con el mayor valor es el total general
        # (las anteriores son subtotales por región)
        return max(totals)
    except Exception:
        return None


def _fetch_stock_json(date_str: str) -> float | None:
    """Parse inventarios desde endpoint JSON (pre nov-2025)."""
    data = _get_json(STOCK_URL_OLD.format(date=date_str))
    if data is None:
        return None

    records = data.get("o_cursor", [])
    cu = [
        x for x in records
        if str(x.get("VARID", "")).strip().lower() == "cu"
    ]

    # Buscar registro de total general (合计)
    for rec in cu:
        name = str(rec.get("WHABBRNAME", "")).strip()
        if "合计" in name:
            region = str(rec.get("REGNAME", "")).strip()
            # El total general no tiene región o tiene "合计" en REGNAME
            if "合计" in region or region == "":
                wt = rec.get("WRTWGHTS")
                if wt is not None:
                    return float(wt)

    # Fallback: sumar todos los subtotales por región
    subtotals = []
    for rec in cu:
        name = str(rec.get("WHABBRNAME", "")).strip()
        if "合计" in name or "Subtotal" in name:
            wt = rec.get("WRTWGHTS")
            if wt is not None:
                subtotals.append(float(wt))
    return sum(subtotals) if subtotals else None


def fetch_positioning(start: date, end: date) -> pd.DataFrame:
    """
    Descarga posicionamiento top 20 miembros SHFE copper.
    Calcula net = top20 long - top20 short (agregado "cuall").

    Nota: esto NO es equivalente al COT de CFTC (no clasifica por tipo
    de participante). Es el agregado de los 20 mayores FCMs.
    """
    rows = []
    dates = _trading_dates(start, end)
    print(f"Descargando posicionamiento SHFE: probando {len(dates)} fechas")

    for d in dates:
        date_str = d.strftime("%Y%m%d")
        data = _get_json(RANK_URL.format(date=date_str))
        if data is None:
            continue

        records = data.get("o_cursor", [])
        # Buscar el registro "cuall" con RANK == 0 (total top 20)
        # o el último registro cuall que tiene el total
        cuall = [
            x for x in records
            if str(x.get("INSTRUMENTID", "")).strip().lower() == "cuall"
            and x.get("RANK") == 0
        ]

        if not cuall:
            # Fallback: buscar rank == -1 (header) que a veces tiene el total
            cuall = [
                x for x in records
                if str(x.get("INSTRUMENTID", "")).strip().lower() == "cuall"
                and x.get("RANK") == -1
            ]

        if not cuall:
            continue

        rec = cuall[0]
        long_oi = rec.get("CJ2")  # top 20 long OI
        short_oi = rec.get("CJ3")  # top 20 short OI

        if long_oi is None or short_oi is None:
            continue

        rows.append({
            "trade_date": d,
            "spread_id": "shfe_cu_top20_net",
            "value": float(long_oi) - float(short_oi),
            "unit": "lots",
        })

    df = pd.DataFrame(rows)
    if not df.empty:
        print(f"  {len(df)} días de posicionamiento obtenidos")
        latest = df.iloc[-1]
        print(f"  Último: {latest['trade_date']} top20 net = {latest['value']:.0f} lots")
    else:
        print("  Sin datos de posicionamiento")
    return df


def main():
    parser = argparse.ArgumentParser(description="Fetch SHFE copper data")
    parser.add_argument("--days", type=int, default=30, help="Días hacia atrás (default: 30)")
    parser.add_argument("--start", type=str, help="Fecha inicio (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, help="Fecha fin (YYYY-MM-DD)")
    parser.add_argument("--no-stocks", action="store_true", help="Skip inventarios (lento)")
    args = parser.parse_args()

    if args.start:
        start = date.fromisoformat(args.start)
        end = date.fromisoformat(args.end) if args.end else date.today()
    else:
        end = date.today()
        start = end - timedelta(days=args.days)

    con = connect(DB_PATH)

    # 1. Precios
    prices_df = fetch_daily_prices(start, end)
    if not prices_df.empty:
        raw_df = prices_df[["series_id", "trade_date", "close", "unit"]].copy()
        raw_df["value"] = raw_df["close"]
        ingest_raw(con, source="shfe", df=raw_df, notes=f"SHFE Cu prices {start} to {end}")

        clean_df = prices_df[["trade_date", "series_id", "close", "high", "low", "volume", "unit"]].copy()
        upsert_prices(con, clean_df)
        print(f"  → {len(clean_df)} filas upserted a clean.prices")

    # 2. Inventarios
    if not args.no_stocks:
        inv_df = fetch_inventories(start, end)
        if not inv_df.empty:
            raw_inv = inv_df.copy()
            raw_inv["series_id"] = "shfe_stocks"
            raw_inv["value"] = raw_inv["volume_mt"]
            raw_inv["unit"] = "metric_tons"
            ingest_raw(con, source="shfe", df=raw_inv, notes=f"SHFE Cu stocks {start} to {end}")
            upsert_inventories(con, inv_df)
            print(f"  → {len(inv_df)} filas upserted a clean.inventories")

    # 3. Posicionamiento
    pos_df = fetch_positioning(start, end)
    if not pos_df.empty:
        upsert_spreads(con, pos_df)
        print(f"  → {len(pos_df)} filas upserted a clean.spreads")

    # Resumen
    print("\nEstado SHFE en DB:")
    try:
        summary = con.execute("""
            SELECT series_id, min(trade_date) AS desde, max(trade_date) AS hasta, count(*) AS n
            FROM clean.prices WHERE series_id LIKE 'shfe%'
            GROUP BY series_id ORDER BY series_id
        """).fetchdf()
        if not summary.empty:
            print(summary.to_string(index=False))
    except Exception:
        pass

    try:
        inv_summary = con.execute("""
            SELECT exchange, category, min(trade_date) AS desde, max(trade_date) AS hasta, count(*) AS n
            FROM clean.inventories WHERE exchange = 'shfe'
            GROUP BY exchange, category
        """).fetchdf()
        if not inv_summary.empty:
            print(inv_summary.to_string(index=False))
    except Exception:
        pass

    con.close()


if __name__ == "__main__":
    main()
