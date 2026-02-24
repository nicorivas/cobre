---
nombre: analisis-semanal
descripcion: Revisión semanal estándar del mercado del cobre
ruta: analisis-semanal
contexto_condicional:
  - si: movimiento_precio > 3%
    agregar: [derivados/opciones-y-volatilidad, tecnico/senales]
  - si: noticia_china_relevante
    agregar: [macro/china]
  - si: noticia_geopolitica_relevante
    agregar: [macro/geopolitica]
inputs:
  - datos de la semana (precios, inventarios, COT, noticias)
outputs:
  - resumen semanal con conclusión bullish/bearish/neutral
  - temas a vigilar para la semana siguiente
---

# Skill: Análisis Semanal

## Procedimiento

### 1. Precios
- Registrar precio de cierre LME cash, 3M, y COMEX
- Calcular cambio semanal (% y absoluto)
- Notar el rango high-low de la semana
- ¿Precio rompió algún nivel técnico clave?

### 2. Estructura de término
- Registrar cash-3M spread LME
- ¿Se amplió o estrechó vs semana anterior?
- ¿Backwardation o contango? ¿Intensificando o moderando?
- Relación con movimiento de inventarios

### 3. Inventarios
- LME: total, on-warrant, cancelled warrants — cambio semanal
- COMEX: registered, eligible — cambio semanal
- SHFE: stocks — cambio semanal
- ¿Algún movimiento inusual? (>10kt en una semana para LME es notable)
- Calcular days of coverage aproximado

### 4. Posicionamiento
- CFTC COT: managed money net position y cambio semanal
- ¿En zona de extremo? (>80th o <20th percentil histórico)
- ¿La dirección del posicionamiento confirma o contradice el movimiento de precio?
- COMEX total OI: ¿creciendo o cayendo?

### 5. Premiums
- Yangshan premium: nivel y cambio
- Rotterdam y Midwest: si disponibles
- COMEX-LME arb: nivel actual
- LME-SHFE import arb: ¿abierta o cerrada?

### 6. Técnico
- ¿Precio por encima/debajo de 50/200 SMA?
- RSI: ¿sobrecomprado, sobrevendido, o neutral?
- ¿Alguna señal técnica relevante? (cross, divergencia, breakout)

### 7. Noticias de la semana
- Revisar `noticias/temas-activos.md`
- ¿Algún tema nuevo? ¿Alguno resuelto?
- ¿Algún dato macro relevante? (PMI, China imports, etc.)

### 8. Síntesis
- Conclusión: **bullish / bearish / neutral** para la semana siguiente
- Justificación en 2-3 oraciones
- Temas a vigilar
- ¿Algún riesgo de evento binario próximo? (FOMC, PMI, tariff decision)
