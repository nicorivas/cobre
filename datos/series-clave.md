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
