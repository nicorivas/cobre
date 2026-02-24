#!/usr/bin/env python3
"""
Descarga precios LME Copper (Cash, 3M) e inventarios desde Westmetall.

Fuente: westmetall.com — publica datos LME oficiales con 1 día de delay.
Datos desde 2008. No requiere API key.

Uso:
    python datos/scripts/fetch_lme.py               # todo lo disponible (~2008-presente)
    python datos/scripts/fetch_lme.py --years 2     # últimos 2 años
"""

import argparse
import sys
from datetime import date, datetime
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).resolve().parent))
from db import connect, ingest_raw, upsert_prices, upsert_inventories, DB_PATH

URL = "https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Cu_cash"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}


def parse_number(s: str) -> float | None:
    """Parsea números con formato europeo (puntos como separador de miles)."""
    s = s.strip().replace(",", "")
    try:
        return float(s)
    except (ValueError, TypeError):
        return None


def parse_date(s: str) -> date | None:
    """Parsea fechas formato '23. February 2026'."""
    s = s.strip().rstrip(".")
    for fmt in ["%d. %B %Y", "%d %B %Y"]:
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None


def fetch_lme(min_year: int | None = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Descarga datos LME de Westmetall.

    Retorna (prices_df, inventories_df).
    """
    print(f"Descargando datos LME desde Westmetall...")
    r = requests.get(URL, headers=HEADERS, timeout=30)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")
    tables = soup.find_all("table")
    print(f"  {len(tables)} tablas encontradas (años)")

    price_rows = []
    inv_rows = []

    for table in tables:
        for tr in table.find_all("tr"):
            cells = [td.get_text(strip=True) for td in tr.find_all("td")]
            if len(cells) < 4 or cells[0] == "date":
                continue

            trade_date = parse_date(cells[0])
            if trade_date is None:
                continue

            if min_year and trade_date.year < min_year:
                continue

            cash = parse_number(cells[1])
            three_m = parse_number(cells[2])
            stock = parse_number(cells[3])

            if cash is not None:
                price_rows.append({
                    "trade_date": trade_date,
                    "series_id": "lme_cash",
                    "close": cash,
                    "unit": "usd_per_ton",
                })
            if three_m is not None:
                price_rows.append({
                    "trade_date": trade_date,
                    "series_id": "lme_3m",
                    "close": three_m,
                    "unit": "usd_per_ton",
                })
            if stock is not None:
                inv_rows.append({
                    "trade_date": trade_date,
                    "exchange": "lme",
                    "category": "total",
                    "volume_mt": stock,
                })

    prices_df = pd.DataFrame(price_rows)
    inv_df = pd.DataFrame(inv_rows)

    print(f"  Precios: {len(prices_df)} filas ({len(prices_df)//2} días × 2 series)")
    print(f"  Inventarios: {len(inv_df)} filas")

    return prices_df, inv_df


def main():
    parser = argparse.ArgumentParser(description="Fetch LME copper data from Westmetall")
    parser.add_argument("--years", type=int, help="Limitar a últimos N años")
    args = parser.parse_args()

    min_year = date.today().year - args.years + 1 if args.years else None

    prices_df, inv_df = fetch_lme(min_year)

    if prices_df.empty:
        print("Sin datos de precios.")
        return

    con = connect(DB_PATH)

    # Raw — precios
    raw_prices = prices_df.copy()
    raw_prices["value"] = raw_prices["close"]
    ingest_raw(con, source="westmetall", df=raw_prices, notes="LME Cu cash + 3M")

    # Raw — inventarios
    if not inv_df.empty:
        raw_inv = inv_df.copy()
        raw_inv["series_id"] = "lme_stocks_total"
        raw_inv["value"] = raw_inv["volume_mt"]
        raw_inv["trade_date"] = raw_inv["trade_date"]
        raw_inv["unit"] = "metric_tons"
        ingest_raw(con, source="westmetall", df=raw_inv, notes="LME Cu stocks")

    # Clean — precios
    upsert_prices(con, prices_df)

    # Clean — inventarios
    if not inv_df.empty:
        upsert_inventories(con, inv_df)

    # Resumen
    summary = con.execute("""
        SELECT series_id, min(trade_date) AS desde, max(trade_date) AS hasta, count(*) AS n
        FROM clean.prices
        WHERE series_id IN ('lme_cash', 'lme_3m')
        GROUP BY series_id
        ORDER BY series_id
    """).fetchdf()
    print(f"\nPrecios LME en clean.prices:")
    print(summary.to_string(index=False))

    inv_summary = con.execute("""
        SELECT exchange, category, min(trade_date) AS desde, max(trade_date) AS hasta, count(*) AS n
        FROM clean.inventories
        WHERE exchange = 'lme'
        GROUP BY exchange, category
    """).fetchdf()
    if not inv_summary.empty:
        print(f"\nInventarios LME en clean.inventories:")
        print(inv_summary.to_string(index=False))

    con.close()


if __name__ == "__main__":
    main()
