---
nodo: tecnico/indicadores
---

# Indicadores Técnicos para Cobre

## Medias Móviles

### SMA (Simple Moving Average)

| Período | Uso | Señal |
|---|---|---|
| **20 SMA** | Tendencia de corto plazo | Precio > 20SMA = momentum positivo CP |
| **50 SMA** | Tendencia de medio plazo | Benchmark de intermediarios |
| **100 SMA** | Tendencia intermedia | Filtro de dirección |
| **200 SMA** | Tendencia de largo plazo | Por encima = bull market; por debajo = bear market |

### EMA (Exponential Moving Average)
- Más peso a datos recientes → reacciona más rápido
- 12 y 26 EMA usadas para construir el MACD
- Preferidas por traders de corto plazo

### Cruces de medias
- **Golden cross**: 50 SMA cruza por encima de 200 SMA → bullish de largo plazo
- **Death cross**: 50 SMA cruza por debajo de 200 SMA → bearish de largo plazo
- Para cobre: los cruces tienen buen track record como señales de tendencia multi-mes

## RSI (Relative Strength Index)

- Período estándar: 14
- Rango: 0-100

| Nivel | Interpretación |
|---|---|
| > 70 | Sobrecomprado (posible corrección) |
| 50-70 | Alcista |
| 30-50 | Bajista |
| < 30 | Sobrevendido (posible rebote) |

- **Divergencias**: RSI hace nuevo mínimo/máximo que el precio no confirma → señal de reversión
- En cobre: RSI > 75 o < 25 son niveles más extremos y confiables

## MACD (Moving Average Convergence Divergence)

```
MACD Line = EMA(12) - EMA(26)
Signal Line = EMA(9) del MACD Line
Histogram = MACD Line - Signal Line
```

- MACD cruza por encima de Signal → bullish
- MACD cruza por debajo de Signal → bearish
- Histogram expandiéndose → momentum acelerando
- Divergencias MACD-precio → cambio de tendencia inminente

## ADX (Average Directional Index)

| ADX | Interpretación |
|---|---|
| < 20 | Sin tendencia (mercado en rango) |
| 20-40 | Tendencia establecida |
| > 40 | Tendencia fuerte |
| > 60 | Tendencia extrema (raro, insostenible) |

- No indica dirección, solo fuerza de tendencia
- ADX subiendo desde < 20 → inicio de nueva tendencia (buscar dirección en +DI/-DI)
- Útil para decidir si usar estrategias de tendencia o de rango

## Bollinger Bands

```
Banda superior = SMA(20) + 2 × σ(20)
Banda media = SMA(20)
Banda inferior = SMA(20) - 2 × σ(20)
```

- Precio tocando banda superior → posible sobreextensión
- Precio tocando banda inferior → posible sobreextensión bajista
- **Squeeze**: bandas se contraen → baja volatilidad → breakout inminente
- **Bandwidth** como indicador de volatilidad realizada

## Ichimoku Cloud

Componentes:
- **Tenkan-sen** (9): línea de conversión (corto plazo)
- **Kijun-sen** (26): línea base (medio plazo)
- **Senkou Span A y B**: forman la nube (cloud)
- **Chikou Span** (26 atrás): confirmación

Señales:
- Precio por encima de la nube = bullish; por debajo = bearish
- Nube verde (A > B) = bullish; nube roja (B > A) = bearish
- Cruces Tenkan/Kijun = señales de entrada/salida

## Volumen y Open Interest

| Combinación | Interpretación |
|---|---|
| Precio ↑ + Volumen ↑ + OI ↑ | Tendencia alcista fuerte (dinero nuevo entrando) |
| Precio ↑ + Volumen ↑ + OI ↓ | Short covering (rally temporal) |
| Precio ↓ + Volumen ↑ + OI ↑ | Tendencia bajista fuerte (nueva venta) |
| Precio ↓ + Volumen ↑ + OI ↓ | Long liquidation (venta forzada) |
| Bajo volumen en cualquier movimiento | Movimiento débil, poca convicción |
