---
nodo: derivados/coberturas
---

# Coberturas (Hedging) de Cobre

## Principio

Hedging = tomar una posición en derivados opuesta a la exposición física, para reducir
la variabilidad del resultado financiero.

## Perfiles de exposición

| Participante | Exposición natural | Hedge |
|---|---|---|
| **Productor** (minera) | Long cobre (va a vender) | Vender futuros / comprar puts |
| **Consumidor** (fabricante) | Short cobre (va a comprar) | Comprar futuros / comprar calls |
| **Smelter** | Spread (compra concentrado, vende cátodo) | Hedge el timing mismatch |
| **Trader** | Variable (depende del libro) | Delta hedging continuo |

## Instrumentos de cobertura

### Futuros (back-to-back hedge)
- Más simple y líquido
- Fija precio exacto (elimina upside y downside)
- Requiere margen y exposición a margin calls
- Basis risk si el hedge no matchea exactamente la exposición

### Opciones

| Estrategia | Costo | Protección | Participación |
|---|---|---|---|
| Long put (productor) | Paga premium | Suelo de precio | Retiene upside |
| Long call (consumidor) | Paga premium | Techo de precio | Retiene downside benefit |
| Collar | Premium neto bajo/cero | Suelo y techo | Acotada en ambas direcciones |
| Put spread | Premium reducido | Protección parcial | — |

### Swaps OTC
- Cash-settled contra promedio de LME del mes
- Customizable en tenor, volumen, pricing
- Riesgo de contraparte (mitigable con ISDA/CSA)
- Para hedging de presupuesto o pricing de largo plazo

## Hedge ratio

### Ratio 1:1 (naive hedge)
- 100% de la exposición cubierta con el mismo volumen en derivados
- Simple pero no siempre óptimo (basis risk, costos de roll)

### Minimum Variance Hedge Ratio

```
h* = ρ × (σ_spot / σ_futures)

Donde:
  ρ = correlación entre cambios de spot y futures
  σ_spot = volatilidad de spot
  σ_futures = volatilidad de futures
```

- Minimiza la varianza de la posición combinada
- Para cobre LME-Grade A: h* ≈ 0.95-1.0 (alta correlación spot-futures)
- Para exposición a scrap o premiums: h* puede ser < 0.8 (mayor basis risk)

### Modelos avanzados

| Modelo | Ventaja | Uso |
|---|---|---|
| **OLS** | Simple, fácil de implementar | Baseline |
| **DCC-GARCH** | Captura correlaciones dinámicas | Cuando correlación varía en el tiempo |
| **Copula-GJR-VAR** | Captura asimetría y dependencia en colas | Mayor precisión en eventos extremos |

## Basis risk

```
Basis = Precio spot de la exposición - Precio del instrumento de hedge
```

Fuentes de basis risk en cobre:
- **Temporal**: QP de la compra/venta no matchea exactamente el vencimiento del futuro
- **Locación**: premium regional no cubierto por LME/COMEX
- **Calidad**: off-grade o scrap vs Grade A del futuro
- **Cross-exchange**: hedge en COMEX pero exposición real referenciada a LME

## Decisiones clave de hedging

1. **¿Cuánto cubrir?** (0-100% de la exposición)
2. **¿Con qué instrumento?** (futuros, opciones, swaps)
3. **¿En qué bolsa?** (LME, COMEX → basis risk cross-exchange)
4. **¿Qué tenor?** (corto plazo, largo plazo, strip)
5. **¿Cuándo ejecutar?** (all-at-once vs layering over time)
6. **¿Cuándo rollar?** (antes del vencimiento, timing del roll)

## Hedge effectiveness testing

Para contabilidad de coberturas (IFRS 9 / ASC 815):
- El hedge debe ser "highly effective" (cambio en instrumento de hedge compensa 80-125% del cambio en exposición)
- Requiere documentación formal y testing periódico
- Métodos: dollar-offset, regression analysis, VaR-based
