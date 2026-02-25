#!/usr/bin/env python3
"""
Descarga precios de COMEX HG Copper, DXY, Gold, US 10Y, S&P 500 via yfinance.

Uso:
    python datos/scripts/fetch_comex.py              # últimos 30 días
    python datos/scripts/fetch_comex.py --days 365   # último año
    python datos/scripts/fetch_comex.py --start 2024-01-01 --end 2024-12-31
"""

import argparse
import sys
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import yfinance as yf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from db import connect, ingest_raw, upsert_prices, DB_PATH

# Mapeo de tickers yfinance → series_id en nuestra base
TICKERS = {
    "HG=F": {
        "series_id": "comex_hg",
        "unit": "usd_per_lb",
        "name": "COMEX HG Copper",
    },
    "DX-Y.NYB": {
        "series_id": "dxy",
        "unit": "index",
        "name": "US Dollar Index",
    },
    "GC=F": {
        "series_id": "gold",
        "unit": "usd_per_oz",
        "name": "Gold Futures",
    },
    "^TNX": {
        "series_id": "us_10y",
        "unit": "pct",
        "name": "US 10Y Yield",
    },
    "^GSPC": {
        "series_id": "sp500",
        "unit": "index",
        "name": "S&P 500",
    },
    "CNY=X": {
        "series_id": "usdcny",
        "unit": "rate",
        "name": "USD/CNY Exchange Rate",
    },
}


def fetch(start: date, end: date) -> pd.DataFrame:
    """Descarga datos de yfinance y retorna DataFrame normalizado."""
    tickers_str = " ".join(TICKERS.keys())
    print(f"Descargando {tickers_str}")
    print(f"  Período: {start} → {end}")

    # yfinance end es exclusivo, sumar un día
    raw = yf.download(
        tickers_str,
        start=str(start),
        end=str(end + timedelta(days=1)),
        auto_adjust=True,
        progress=False,
    )

    if raw.empty:
        print("No se obtuvieron datos.")
        return pd.DataFrame()

    rows = []
    for ticker, meta in TICKERS.items():
        try:
            # yfinance con múltiples tickers retorna MultiIndex columns
            if isinstance(raw.columns, pd.MultiIndex):
                close = raw[("Close", ticker)].dropna()
                high = raw[("High", ticker)].dropna()
                low = raw[("Low", ticker)].dropna()
                volume = raw[("Volume", ticker)].dropna() if ("Volume", ticker) in raw.columns else pd.Series(dtype=float)
            else:
                # Un solo ticker
                close = raw["Close"].dropna()
                high = raw["High"].dropna()
                low = raw["Low"].dropna()
                volume = raw["Volume"].dropna() if "Volume" in raw.columns else pd.Series(dtype=float)

            for dt in close.index:
                row = {
                    "series_id": meta["series_id"],
                    "trade_date": dt.date() if hasattr(dt, "date") else dt,
                    "value": float(close.loc[dt]),
                    "close": float(close.loc[dt]),
                    "unit": meta["unit"],
                }
                if dt in high.index:
                    row["high"] = float(high.loc[dt])
                if dt in low.index:
                    row["low"] = float(low.loc[dt])
                if dt in volume.index:
                    row["volume"] = float(volume.loc[dt])
                rows.append(row)

            print(f"  {meta['name']}: {len(close)} puntos")
        except Exception as e:
            print(f"  {meta['name']}: ERROR — {e}")

    if not rows:
        return pd.DataFrame()

    df = pd.DataFrame(rows)
    df["trade_date"] = pd.to_datetime(df["trade_date"]).dt.date
    return df


def main():
    parser = argparse.ArgumentParser(description="Fetch COMEX + market data via yfinance")
    parser.add_argument("--days", type=int, default=30, help="Días hacia atrás (default: 30)")
    parser.add_argument("--start", type=str, help="Fecha inicio (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, help="Fecha fin (YYYY-MM-DD)")
    args = parser.parse_args()

    if args.start:
        start = date.fromisoformat(args.start)
        end = date.fromisoformat(args.end) if args.end else date.today()
    else:
        end = date.today()
        start = end - timedelta(days=args.days)

    df = fetch(start, end)
    if df.empty:
        print("Sin datos para ingestar.")
        return

    con = connect(DB_PATH)

    # 1. Raw (inmutable)
    raw_df = df[["series_id", "trade_date", "value", "unit"]].copy()
    for col in ["high", "low", "volume"]:
        if col in df.columns:
            raw_df[col] = df[col]
    ingestion_id = ingest_raw(con, source="yfinance", df=raw_df, notes=f"{start} to {end}")
    print(f"\nRaw: ingestion_id={ingestion_id}, {len(raw_df)} filas")

    # 2. Clean (upsert)
    clean_df = df[["trade_date", "series_id", "close", "unit"]].copy()
    for col in ["high", "low", "volume"]:
        if col in df.columns:
            clean_df[col] = df[col]
    upsert_prices(con, clean_df)
    print(f"Clean: {len(clean_df)} filas upserted a clean.prices")

    # 3. Resumen
    summary = con.execute(
        "SELECT series_id, min(trade_date) AS desde, max(trade_date) AS hasta, count(*) AS n FROM clean.prices GROUP BY series_id ORDER BY series_id"
    ).fetchdf()
    print(f"\nEstado de clean.prices:")
    print(summary.to_string(index=False))

    con.close()


if __name__ == "__main__":
    main()
