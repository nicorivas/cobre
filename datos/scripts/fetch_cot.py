#!/usr/bin/env python3
"""
Descarga y parsea el reporte CFTC Commitments of Traders (COT) para cobre.

Fuente: CFTC Disaggregated Futures Only reports.
El reporte se publica cada viernes con datos del martes.

Uso:
    python datos/scripts/fetch_cot.py             # año actual
    python datos/scripts/fetch_cot.py --year 2024
"""

import argparse
import io
import sys
import zipfile
from datetime import date
from pathlib import Path

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from db import connect, ingest_raw, upsert_cot, DB_PATH

# CFTC publica reportes anuales en formato zip
# Disaggregated reports tienen la granularidad que necesitamos (managed money)
COT_BASE_URL = "https://www.cftc.gov/files/dea/history/fut_disagg_txt_{year}.zip"

# Copper COMEX: CFTC_Commodity_Code = 85, market name contiene "COPPER"
COPPER_COMMODITY_CODE = 85


def fetch_cot(year: int) -> pd.DataFrame:
    """Descarga el COT disaggregated de un año y extrae copper."""
    url = COT_BASE_URL.format(year=year)
    print(f"Descargando COT {year} desde CFTC...")
    print(f"  URL: {url}")

    resp = requests.get(url, timeout=60)
    resp.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(resp.content)) as zf:
        csv_name = zf.namelist()[0]
        print(f"  Archivo: {csv_name}")
        with zf.open(csv_name) as f:
            df = pd.read_csv(f, low_memory=False)

    # Filtrar solo copper COMEX
    # CFTC_Commodity_Code es numérico (85) para copper
    copper = df[
        df["Market_and_Exchange_Names"].str.contains("COPPER", case=False, na=False)
    ].copy()

    if copper.empty:
        print("  No se encontraron datos de cobre.")
        return pd.DataFrame()

    print(f"  {len(copper)} reportes semanales de cobre encontrados")

    # Parsear a nuestro schema
    rows = []
    for _, row in copper.iterrows():
        report_date = pd.to_datetime(row["Report_Date_as_YYYY-MM-DD"]).date()
        rows.append({
            "report_date": report_date,
            "managed_money_long": int(row.get("M_Money_Positions_Long_All", 0)),
            "managed_money_short": int(row.get("M_Money_Positions_Short_All", 0)),
            "managed_money_net": int(row.get("M_Money_Positions_Long_All", 0))
                - int(row.get("M_Money_Positions_Short_All", 0)),
            "producer_long": int(row.get("Prod_Merc_Positions_Long_All", 0)),
            "producer_short": int(row.get("Prod_Merc_Positions_Short_All", 0)),
            "producer_net": int(row.get("Prod_Merc_Positions_Long_All", 0))
                - int(row.get("Prod_Merc_Positions_Short_All", 0)),
            "swap_dealer_long": int(row.get("Swap_Positions_Long_All", 0)),
            "swap_dealer_short": int(row.get("Swap__Positions_Short_All", 0)),
            "swap_dealer_net": int(row.get("Swap_Positions_Long_All", 0))
                - int(row.get("Swap__Positions_Short_All", 0)),
            "total_oi": int(row.get("Open_Interest_All", 0)),
        })

    return pd.DataFrame(rows)


def main():
    parser = argparse.ArgumentParser(description="Fetch CFTC COT data for copper")
    parser.add_argument("--year", type=int, default=date.today().year, help="Año a descargar (default: actual)")
    parser.add_argument("--backfill", type=int, help="Descargar N años hacia atrás")
    args = parser.parse_args()

    years = []
    if args.backfill:
        current_year = date.today().year
        years = list(range(current_year - args.backfill + 1, current_year + 1))
    else:
        years = [args.year]

    con = connect(DB_PATH)
    total = 0

    for year in years:
        df = fetch_cot(year)
        if df.empty:
            continue

        # Raw
        raw_df = df.copy()
        raw_df["series_id"] = "cot_copper"
        raw_df["trade_date"] = raw_df["report_date"]
        raw_df["value"] = raw_df["managed_money_net"]
        raw_df["unit"] = "contracts"
        ingest_raw(con, source="cftc", df=raw_df, notes=f"COT disaggregated {year}")

        # Clean
        upsert_cot(con, df)
        print(f"  → {len(df)} semanas upserted a clean.cot")
        total += len(df)

    # Resumen
    if total > 0:
        summary = con.execute(
            "SELECT min(report_date) AS desde, max(report_date) AS hasta, count(*) AS semanas FROM clean.cot"
        ).fetchdf()
        print(f"\nEstado de clean.cot:")
        print(summary.to_string(index=False))

    con.close()


if __name__ == "__main__":
    main()
