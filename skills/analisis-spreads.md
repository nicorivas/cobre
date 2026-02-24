---
nombre: analisis-spreads
descripcion: Analizar spreads de mercado y oportunidades
nodos:
  - derivados/spreads
  - pricing/estructura-de-termino
  - trading/inventarios
  - derivados/futuros-y-forwards
inputs:
  - datos de spreads (calendar, COMEX-LME, LME-SHFE)
outputs:
  - diagnóstico de cada spread
  - señales de mercado implícitas
  - oportunidades si las hay
---

# Skill: Análisis de Spreads

## Procedimiento

### 1. Calendar spreads
- Registrar front-2nd month y front-back (e.g., 3M-15M)
- ¿Backwardation o contango? ¿Amplificándose o moderándose?
- Comparar con estacionalidad: ¿el movimiento es seasonal o counterseasonal?
- Comparar con inventarios: ¿coherente?

### 2. COMEX-LME Arb
- Calcular: COMEX (en USD/t) - LME
- Nivel actual vs rango histórico
- > $100/t: elevado; > $500/t: distorsionado; > $2,000/t: extremo
- ¿Qué está driving el arb? (tariffs, flujos, demanda regional)
- ¿La tendencia es convergencia o divergencia?

### 3. LME-SHFE Import Arb
- Calcular: (SHFE / USDCNY) - LME cash - estimated costs
- ¿Ventana abierta o cerrada?
- Abierta = rentable importar a China = demanda china fuerte
- Cerrada = no rentable = demanda débil o precios SHFE deprimidos

### 4. Inter-commodity (si aplica)
- Ratio Cu/Al: ¿por encima del rango histórico? (riesgo de sustitución)
- ¿Algún spread inter-commodity en extremo?

### 5. Señales integradas
- Todos los spreads contando la misma historia = alta convicción
- Spreads contradictorios = mercado en transición, cautela

### 6. Oportunidades
- ¿Algún spread en extremo histórico con catalizador de reversión identificable?
- ¿Calendar spread mispriced vs inventarios?
- ¿Arb COMEX-LME tiene potencial de convergencia?
- Considerar margin efficiency de cada spread
