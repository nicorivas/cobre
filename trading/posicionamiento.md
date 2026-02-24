---
nodo: trading/posicionamiento
---

# Posicionamiento Especulativo

## CFTC Commitments of Traders (COT)

### Qué es
- Reporte semanal publicado por la CFTC (viernes, datos del martes)
- Desglosa open interest de COMEX Copper por categoría de participante
- Gratis, descargable de cftc.gov

### Categorías relevantes

| Categoría | Quiénes son | Comportamiento |
|---|---|---|
| **Producer/Merchant** | Mineras, consumidores, trading houses | Hedgers naturales; posición típica: net short |
| **Swap Dealers** | Bancos, dealers OTC | Intermediarios; posición neta varía |
| **Managed Money** | Hedge funds, CTAs, commodity pools | Especuladores; la categoría más monitoreada |
| **Other Reportables** | Entidades grandes no clasificadas | Mixto |

### Managed Money: la señal clave

```
Net Position = Longs - Shorts (managed money)
```

| Nivel net longs | Señal |
|---|---|
| Máximos históricos (>80k contratos) | Mercado crowded long; riesgo de liquidación |
| Positivo moderado (30-60k) | Sentimiento alcista pero no extremo |
| Cerca de cero | Neutral |
| Negativo (<0) | Sentimiento bearish; posible señal contrarian de compra |
| Mínimos históricos | Extremo bearish; señal contrarian fuerte |

### Señales contrarian

El COT funciona mejor como indicador **contrarian en extremos**:
- Máximo histórico de net longs → probabilidad elevada de corrección
- Mínimo histórico de net longs → probabilidad elevada de rebote
- En zona neutral → poca señal

### Ritmo de cambio

El **cambio semanal** en net position puede ser más informativo que el nivel:
- Liquidación rápida (>10k contratos/semana) → presión vendedora adicional
- Acumulación rápida de longs → momentum alcista pero atención al crowding

## Open Interest total

- Open interest creciente + precio subiendo = tendencia fuerte (dinero nuevo entrando)
- Open interest cayendo + precio subiendo = short covering (no tendencia nueva)
- Open interest creciente + precio cayendo = nueva venta, presión bajista
- Open interest cayendo + precio cayendo = long liquidation

## LME Positioning

La LME publica data de posicionamiento menos granular:
- **COTR (Commitment of Traders Report)**: categorías investment fund, commercial, other
- Menos detallado que CFTC pero cubre LME-specific positioning
- Publicado semanalmente

## Uso analítico

1. **Contexto**: ¿El movimiento de precio está respaldado por flujos de posicionamiento?
2. **Extremos**: ¿Estamos en niveles de crowding que señalan reversión?
3. **Divergencias**: ¿Precio subiendo pero managed money reduciendo longs? Bearish.
4. **Confirmación**: OI + precio + posicionamiento coherentes = mayor convicción en la tendencia
