---
nodo: datos/series-clave
---

# Series de Datos Clave para Monitoreo

## Precio

| Serie | Fuente | Frecuencia | Importancia |
|---|---|---|---|
| LME Copper Cash Settlement | LME | Diario | Referencia global #1 |
| LME Copper 3-Month | LME | Diario | Benchmark para contratos físicos |
| COMEX HG Front Month | CME | Diario | Referencia Norteamérica |
| SHFE CU Front Month | SHFE | Diario | Referencia China |

## Estructura de término

| Serie | Fuente | Frecuencia | Importancia |
|---|---|---|---|
| LME Cash - 3M Spread | LME / calculado | Diario | Indicador #1 de tightness |
| COMEX Front - 2nd Month Spread | CME / calculado | Diario | Calendar spread US |
| LME Forward Curve (full) | LME | Diario | Shape de la curva completa |

## Inventarios

| Serie | Fuente | Frecuencia | Importancia |
|---|---|---|---|
| LME Total Stocks | LME | Diario | Inventarios visibles #1 |
| LME On-Warrant Stocks | LME | Diario | Stock realmente disponible |
| LME Cancelled Warrants | LME | Diario | Leading indicator de drawdowns |
| COMEX Registered + Eligible | CME | Diario | Inventarios US |
| SHFE Stocks | SHFE | Semanal (viernes) | Inventarios China |
| China Bonded Stocks (estimado) | CRU/SMM | Semanal | Inventarios invisibles China |

## Posicionamiento

| Serie | Fuente | Frecuencia | Importancia |
|---|---|---|---|
| CFTC COT - Managed Money Net Position | CFTC | Semanal (viernes) | Sentimiento especulativo |
| CFTC COT - Producer Net Position | CFTC | Semanal | Hedging de productores |
| COMEX Total Open Interest | CME | Diario | Participación total en mercado |

## Premiums y spreads

| Serie | Fuente | Frecuencia | Importancia |
|---|---|---|---|
| Yangshan Premium | SMM / Fastmarkets | Diario | Demanda china de importación |
| Rotterdam CIF Premium | Fastmarkets / Platts | Semanal | Condiciones mercado europeo |
| US Midwest Premium | Fastmarkets | Semanal | Condiciones mercado US |
| COMEX-LME Arb | Calculado | Diario | Flujos US, tariff expectations |
| LME-SHFE Import Arb | Calculado | Diario | Window de importación China |
| TC/RC Spot | Fastmarkets | Semanal | Tightness de concentrado |

## Macro

| Serie | Fuente | Frecuencia | Importancia |
|---|---|---|---|
| PMI Caixin Manufacturing China | Caixin/S&P | Mensual | Leading indicator #1 |
| ISM Manufacturing US | ISM | Mensual | Actividad industrial US |
| DXY (Dollar Index) | ICE / Bloomberg | Diario | Correlación inversa con Cu |
| China Total Social Financing | PBOC | Mensual | Para calcular credit impulse |
| China Copper Imports (refined) | GACC | Mensual | Demanda directa |
| China Copper Conc. Imports | GACC | Mensual | Demanda de fundiciones |

## Checklist de monitoreo diario mínimo

1. LME Cash & 3M prices + Cash-3M spread
2. COMEX HG settlement
3. LME stocks (total, on-warrant, cancelled warrants)
4. COMEX stocks (registered + eligible)
5. COMEX-LME arb

## Checklist semanal adicional

6. SHFE stocks
7. CFTC COT (managed money net position)
8. Yangshan premium
9. TC/RC spot (Fastmarkets)
10. Noticias clave de la semana

## Disponibilidad en el pipeline

Las series marcadas con **P** están disponibles automáticamente via el pipeline
(`datos/scripts/fetch_all.py`). Las marcadas con **M** requieren ingreso manual
o suscripción de pago.

| Serie | `series_id` en DuckDB | Disponibilidad |
|---|---|---|
| LME Cash Settlement | `lme_cash` | **P** — `fetch_lme.py` |
| LME 3-Month | `lme_3m` | **P** — `fetch_lme.py` |
| COMEX HG Front Month | `comex_hg` (USD/lb), `comex_hg_ton` (USD/ton) | **P** — `fetch_comex.py` |
| LME Total Stocks | `clean.inventories` (lme, total) | **P** — `fetch_lme.py` |
| CFTC COT Managed Money | `clean.cot` | **P** — `fetch_cot.py` |
| DXY | `dxy` | **P** — `fetch_comex.py` |
| Gold | `gold` | **P** — `fetch_comex.py` |
| US 10Y Yield | `us_10y` | **P** — `fetch_comex.py` |
| S&P 500 | `sp500` | **P** — `fetch_comex.py` |
| Fed Funds Rate | `fed_funds` | **P** — `fetch_fred.py` |
| Industrial Production | `indpro` | **P** — `fetch_fred.py` |
| LME Cash-3M Spread | `lme_cash_3m` | **P** — `calc_spreads.py` |
| COMEX-LME Arb | `comex_lme_arb` | **P** — `calc_spreads.py` |
| Cu/Au Ratio | `cu_au_ratio` | **P** — `calc_spreads.py` |
| SHFE CU Front Month | `shfe_cu` (RMB/t), `shfe_cu_ton` (USD/t) | **P** — `fetch_shfe.py` |
| SHFE Stocks | `clean.inventories` (shfe, total) | **P** — `fetch_shfe.py` |
| SHFE Top 20 Net Position | `shfe_cu_top20_net` | **P** — `fetch_shfe.py` |
| USD/CNY | `usdcny` | **P** — `fetch_comex.py` |
| LME-SHFE Import Arb | `lme_shfe_arb` | **P** — `calc_spreads.py` |
| Yangshan Premium | — | **M** — Fastmarkets/SMM (pago) |
| TC/RC Spot | — | **M** — Fastmarkets (pago) |
| Premiums (Rotterdam, Midwest) | — | **M** — Fastmarkets/Platts (pago) |
| COMEX Stocks (registered/eligible) | — | **M** — CME web (pendiente) |
| PMI Caixin / ISM | — | **M** — ISM no publica en FRED |
