---
nodo: derivados/spreads
---

# Spreads en el Mercado del Cobre

## Calendar Spreads (Intra-market)

### Concepto
Compra de un mes y venta de otro mes en la misma bolsa.

Ejemplo: Long COMEX March / Short COMEX August

### Ventajas
- **Margin reducido**: ~$200/lot vs miles para outright (CME inter-month spread credit)
- **Menor volatilidad**: movimiento más suave y tendencial que outright
- **Puro reflejo de fundamentales**: spot supply/demand → nearby, expectativas → deferred

### Estacionalidad
- Q1-Q2: tendencia a backwardation (demanda de construcción, restocking China)
- Q4: tendencia a contango (supply acumulado, demanda modera)
- Alrededor de marzo: construcción ramps up → front month sube más que deferred

### Análisis

```
Spread = Precio contrato cercano - Precio contrato lejano
```

| Spread | Estructura | Señal |
|---|---|---|
| Positivo y ampliándose | Backwardation profundizando | Tightness creciente |
| Positivo y estrechándose | Backwardation reduciendo | Tightness aliviando |
| Negativo y ampliándose | Contango profundizando | Surplus creciente |
| Negativo y estrechándose | Contango reduciendo | Surplus aliviando |

## Inter-Exchange Spreads

### COMEX-LME Arb

```
Arb = Precio COMEX (USD/t) - Precio LME (USD/t)
```

| Nivel | Significado |
|---|---|
| ~$50-100/t | Normal (refleja transporte, handling) |
| > $500/t | Distorsión significativa (tariffs, flujos anormales) |
| > $2,000/t | Extremo (como en 2025 por expectativas de tariff) |

Componentes del arb:
- Costo de transporte (flete marítimo)
- Seguros y handling
- Tariff expectations (el mayor driver en 2025)
- Diferencias de oferta/demanda regional

Oportunidad: cuando el arb excede los costos de transporte + tariff → profitable to ship metal.

### LME-SHFE Arb

```
Import arb = (SHFE / USDCNY) - LME cash - Premium
```

| Ventana | Significado |
|---|---|
| **Abierta** (SHFE > LME + costos) | Rentable importar a China; señal de demanda china fuerte |
| **Cerrada** (SHFE < LME + costos) | No rentable importar; señal de demanda china débil |

Es uno de los indicadores más seguidos de demanda china real en tiempo casi real.

## Inter-Commodity Spreads

### Cobre-Aluminio
- Ratio histórico: ~3-4x
- Sustitución es el driver: Cu/Al > 4.5x incentiva sustitución de cobre por aluminio
- Trading: long Cu / short Al (o viceversa) para capturar reversión al mean

### Cobre-Zinc
- Ratio más estable históricamente
- Ambos sensibles a construcción y ciclo industrial
- Spread refleja diferencias de balance de mercado entre los dos metales

## Margin efficiency

| Tipo de spread | Margen vs outright | Nota |
|---|---|---|
| Calendar (COMEX) | ~5-15% | Spread credit de CME |
| Calendar (LME) | ~10-20% | Carry credit |
| Inter-exchange | ~50-80% | Sin crédito cross-exchange |
| Inter-commodity | ~30-60% | Correlation credit parcial |

## Riesgos del trading de spreads

- **Ejecución**: legs independientes pueden divergir durante ejecución
- **Basis risk**: para inter-exchange, FX y timing differences
- **Squeeze risk**: una pata del spread puede ser squeezed
- **Liquidez**: back months y cross-exchange pueden ser ilíquidos
