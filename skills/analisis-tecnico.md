---
nombre: analisis-tecnico
descripcion: Evaluar señales técnicas y niveles clave del cobre
nodos:
  - tecnico/indicadores
  - tecnico/estructura-de-mercado
  - tecnico/senales
inputs:
  - precio actual y datos de precio recientes
  - timeframe principal (daily recomendado)
outputs:
  - niveles clave (soporte, resistencia)
  - estado de indicadores
  - señales activas si las hay
---

# Skill: Análisis Técnico

## Procedimiento

### 1. Contexto de tendencia
- ¿Precio por encima o debajo de 200 SMA? → bull vs bear market de largo plazo
- ¿Precio por encima o debajo de 50 SMA? → tendencia de medio plazo
- ¿20 > 50 > 100 > 200? (uptrend ordenado) o al revés (downtrend)
- ADX: ¿hay tendencia (>20) o rango (<20)?

### 2. Momentum
- RSI(14): ¿sobrecomprado (>70), sobrevendido (<30), o neutral?
- MACD: ¿por encima o debajo de signal line? ¿Histogram expandiendo o contrayendo?
- ¿Alguna divergencia RSI-precio o MACD-precio?

### 3. Niveles clave
- **Soporte**: mínimos recientes, medias móviles, Fibonacci de última subida
- **Resistencia**: máximos recientes, medias móviles, Fibonacci de última bajada
- **Niveles psicológicos**: números redondos ($4.00, $4.50, $9,000/t, $10,000/t)
- Marcar los 2-3 niveles más importantes en cada dirección

### 4. Patrones
- ¿Hay algún patrón de precio formándose? (H&S, doble techo/piso, triángulo, flag)
- ¿Patrón de continuación o reversión?
- ¿Cerca de breakout? ¿Cuál es el trigger level?

### 5. Volumen y OI
- ¿Volumen confirmando el movimiento de precio?
- ¿OI creciendo (dinero nuevo) o cayendo (posiciones cerrándose)?

### 6. Señales activas
- ¿Golden/death cross reciente o inminente?
- ¿Divergencia activa?
- ¿Bollinger squeeze?
- ¿Breakout de patrón o nivel clave?

### 7. Conclusión técnica
- Bias: bullish / bearish / neutral
- Niveles clave: soporte en [$X], resistencia en [$Y]
- Señal activa: [describir si hay]
- Nota: combinar con fundamentales y posicionamiento para convicción
