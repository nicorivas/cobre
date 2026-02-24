---
nodo: pricing/benchmarks
---

# Benchmarks y Proveedores de Datos de Precio

## Proveedores principales

### Bolsas de futuros (precios de referencia)

| Bolsa | Contrato | Referencia | Frecuencia |
|---|---|---|---|
| LME | Copper Grade A | Official Price, Closing Price | Diario |
| COMEX (CME) | HG Copper | Settlement price | Diario |
| SHFE | CU | Settlement price | Diario |

### Price Reporting Agencies (PRAs)

| PRA | Cobertura | Fortaleza |
|---|---|---|
| **Fastmarkets** (ex-Metal Bulletin + AMM) | Premiums, TC/RC spot, scrap | Referencia global para premiums, TC/RC |
| **Platts** (S&P Global) | Premiums, assessments | Metodología IOSCO-compliant |
| **CRU** | Premiums, TC/RC, análisis | Análisis integrado, modelos de costos |
| **SMM** (Shanghai Metals Market) | Precios domésticos China, premiums, scrap | Referencia para mercado chino |

### Consultoras y research

| Proveedor | Tipo | Cobertura |
|---|---|---|
| **Wood Mackenzie** | Research | Cost curves, análisis por mina, forecasts LP |
| **CRU** | Research + pricing | Copper Monitor (quincenal), forecasts |
| **ICSG** | Estadísticas oficiales | Balance, producción, consumo (mensual) |
| **WBMS** | Estadísticas | Producción, consumo, comercio |
| **Bloomberg** | Terminal | Precios, analytics, posicionamiento |
| **Reuters/Refinitiv** | Terminal | Precios, noticias, analytics |

## Cuál usar para qué

| Necesidad | Fuente recomendada |
|---|---|
| Precio spot/futures de referencia | LME (Global), COMEX (Norteamérica) |
| Premiums físicos | Fastmarkets, Platts |
| TC/RC | Fastmarkets |
| Balance de mercado | ICSG (oficial), CRU/Wood Mac (análisis) |
| Cost curves | Wood Mackenzie, CRU |
| Posicionamiento (COT) | CFTC (gratis, semanal) |
| Inventarios | LME, COMEX, SHFE (gratis, diario) |
| Análisis integrado | CRU Copper Monitor, Bloomberg |
| Precios scrap China | SMM |

## Metodologías de assessment

Las PRAs publican assessments (no precios de transacción) basados en:
- Encuestas a participantes del mercado
- Transacciones reportadas
- Bids y offers observados
- Juicio editorial

Los assessments de Platts y Fastmarkets siguen principios IOSCO para benchmarks.
