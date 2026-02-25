#!/usr/bin/env python3
"""
Calcula spreads y ratios derivados a partir de datos en clean.prices.

Series calculadas:
  - comex_hg_ton: COMEX HG convertido de USD/lb a USD/ton (auxiliar)
  - shfe_cu_ton: SHFE Cu convertido de RMB/ton a USD/ton (auxiliar)
  - cu_au_ratio: Copper/Gold ratio
  - lme_cash_3m: LME Cash - 3M spread (positivo = backwardation)
  - comex_lme_arb: COMEX (en USD/ton) - LME Cash (positivo = COMEX premium)
  - lme_shfe_arb: SHFE (en USD/ton) - LME Cash (positivo = SHFE premium, import arb proxy)

Uso:
    python datos/scripts/calc_spreads.py
"""

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from db import connect, upsert_spreads, upsert_prices, DB_PATH

# Constantes de conversión
LBS_PER_TON = 2204.62
TROY_OZ_PER_TON_GOLD = 32150.7  # no se usa directamente, el ratio es adimensional


def main():
    con = connect(DB_PATH)

    # --- COMEX en USD/ton (auxiliar para comparaciones con LME) ---
    comex_lb = con.execute(
        "SELECT trade_date, close FROM clean.prices WHERE series_id = 'comex_hg' ORDER BY trade_date"
    ).fetchdf()

    if not comex_lb.empty:
        comex_ton = comex_lb.copy()
        comex_ton["series_id"] = "comex_hg_ton"
        comex_ton["close"] = comex_ton["close"] * LBS_PER_TON
        comex_ton["unit"] = "usd_per_ton"
        upsert_prices(con, comex_ton)
        print(f"COMEX USD/ton: {len(comex_ton)} filas → clean.prices")

    # --- SHFE en USD/ton (auxiliar para comparaciones con LME) ---
    shfe_usd = con.execute("""
        SELECT
            shfe.trade_date,
            shfe.close AS shfe_rmb,
            fx.close AS usdcny
        FROM clean.prices shfe
        JOIN clean.prices fx
            ON shfe.trade_date = fx.trade_date
        WHERE shfe.series_id = 'shfe_cu'
          AND fx.series_id = 'usdcny'
          AND fx.close > 0
        ORDER BY shfe.trade_date
    """).fetchdf()

    if not shfe_usd.empty:
        shfe_ton = pd.DataFrame({
            "trade_date": shfe_usd["trade_date"],
            "series_id": "shfe_cu_ton",
            "close": shfe_usd["shfe_rmb"] / shfe_usd["usdcny"],
            "unit": "usd_per_ton",
        })
        upsert_prices(con, shfe_ton)
        print(f"SHFE USD/ton: {len(shfe_ton)} filas → clean.prices")

    # --- Copper/Gold ratio ---
    # Cobre en USD/lb, oro en USD/oz — ratio adimensional
    # Usamos el precio en centavos/lb normalizado contra oz de oro
    # Fórmula estándar: (Cu USD/lb * 1000) / (Au USD/oz)
    # Esto da un ratio ~tipo 4-5 en rangos normales
    prices = con.execute("""
        SELECT
            cu.trade_date,
            cu.close AS cu_price,
            au.close AS au_price
        FROM clean.prices cu
        JOIN clean.prices au
            ON cu.trade_date = au.trade_date
        WHERE cu.series_id = 'comex_hg'
          AND au.series_id = 'gold'
          AND au.close > 0
        ORDER BY cu.trade_date
    """).fetchdf()

    if not prices.empty:
        ratio_df = pd.DataFrame({
            "trade_date": prices["trade_date"],
            "spread_id": "cu_au_ratio",
            "value": (prices["cu_price"] * 1000) / prices["au_price"],
            "unit": "ratio",
        })
        upsert_spreads(con, ratio_df)
        print(f"Cu/Au ratio: {len(ratio_df)} filas → clean.spreads")

    # --- LME Cash - 3M spread (backwardation/contango) ---
    lme_spread = con.execute("""
        SELECT
            cash.trade_date,
            cash.close AS cash_price,
            m3.close AS three_m_price
        FROM clean.prices cash
        JOIN clean.prices m3
            ON cash.trade_date = m3.trade_date
        WHERE cash.series_id = 'lme_cash'
          AND m3.series_id = 'lme_3m'
        ORDER BY cash.trade_date
    """).fetchdf()

    if not lme_spread.empty:
        spread_df = pd.DataFrame({
            "trade_date": lme_spread["trade_date"],
            "spread_id": "lme_cash_3m",
            "value": lme_spread["cash_price"] - lme_spread["three_m_price"],
            "unit": "usd_per_ton",
        })
        upsert_spreads(con, spread_df)
        print(f"LME Cash-3M spread: {len(spread_df)} filas → clean.spreads")

    # --- COMEX-LME Arbitrage ---
    # COMEX (convertido a USD/ton) - LME Cash
    # Positivo = COMEX premium (señal de tariffs, tightness US)
    arb = con.execute("""
        SELECT
            comex.trade_date,
            comex.close AS comex_ton,
            lme.close AS lme_cash
        FROM clean.prices comex
        JOIN clean.prices lme
            ON comex.trade_date = lme.trade_date
        WHERE comex.series_id = 'comex_hg_ton'
          AND lme.series_id = 'lme_cash'
        ORDER BY comex.trade_date
    """).fetchdf()

    if not arb.empty:
        arb_df = pd.DataFrame({
            "trade_date": arb["trade_date"],
            "spread_id": "comex_lme_arb",
            "value": arb["comex_ton"] - arb["lme_cash"],
            "unit": "usd_per_ton",
        })
        upsert_spreads(con, arb_df)
        print(f"COMEX-LME arb: {len(arb_df)} filas → clean.spreads")

    # --- LME-SHFE Import Arb ---
    # SHFE (convertido a USD/ton) - LME Cash
    # Positivo = SHFE premium → import window abierta (rentable importar a China)
    # No incluye costos de transporte ni premium — es un proxy bruto
    lme_shfe = con.execute("""
        SELECT
            shfe.trade_date,
            shfe.close AS shfe_usd,
            lme.close AS lme_cash
        FROM clean.prices shfe
        JOIN clean.prices lme
            ON shfe.trade_date = lme.trade_date
        WHERE shfe.series_id = 'shfe_cu_ton'
          AND lme.series_id = 'lme_cash'
        ORDER BY shfe.trade_date
    """).fetchdf()

    if not lme_shfe.empty:
        lme_shfe_df = pd.DataFrame({
            "trade_date": lme_shfe["trade_date"],
            "spread_id": "lme_shfe_arb",
            "value": lme_shfe["shfe_usd"] - lme_shfe["lme_cash"],
            "unit": "usd_per_ton",
        })
        upsert_spreads(con, lme_shfe_df)
        print(f"LME-SHFE arb: {len(lme_shfe_df)} filas → clean.spreads")

    # --- Resumen ---
    summary = con.execute(
        "SELECT spread_id, min(trade_date) AS desde, max(trade_date) AS hasta, count(*) AS n FROM clean.spreads GROUP BY spread_id ORDER BY spread_id"
    ).fetchdf()
    if not summary.empty:
        print(f"\nEstado de clean.spreads:")
        print(summary.to_string(index=False))

    con.close()


if __name__ == "__main__":
    main()
