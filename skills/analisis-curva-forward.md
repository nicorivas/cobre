---
nombre: analisis-curva-forward
descripcion: Analizar la estructura de término y sus implicaciones
nodos:
  - pricing/estructura-de-termino
  - trading/inventarios
  - derivados/spreads
  - fundamentos/balance-de-mercado
inputs:
  - datos de la curva forward (cash, 3M, 6M, 12M o más)
  - contexto de inventarios actual
outputs:
  - interpretación de la forma de la curva
  - implicaciones para roll yield, hedging, y dirección de precio
---

# Skill: Análisis de Curva Forward

## Procedimiento

### 1. Snapshot de la curva
- Registrar: cash, 3M, 6M, 12M, 24M (lo que esté disponible)
- Calcular spreads: cash-3M, 3M-12M
- Forma general: contango, backwardation, flat, humped

### 2. Comparar con período anterior
- ¿La curva se empinó, aplanó, o invirtió?
- ¿El cambio fue en el front-end (nearby) o back-end (deferred)?
- Front-end driven = factores de spot supply/demand
- Back-end driven = cambio de expectativas de largo plazo

### 3. Theory of storage check
- Inventarios actuales → ¿qué convenience yield implica?
- ¿La estructura de término es coherente con el nivel de inventarios?
- Si inventarios bajos pero contango → posible acumulación invisible o expectativa de resolución

### 4. Roll yield
- Calcular roll yield implícito para posición larga
- Contango: roll cost = erosión para longs (~X%/año)
- Backwardation: roll yield = ganancia para longs (~Y%/año)
- ¿Ha cambiado materialmente? Impacta retornos de posiciones y funds pasivos

### 5. Señales de trading
- ¿Oportunidad en calendar spread? (front vs back mispriced vs fundamentales)
- ¿Backwardation excesiva? (¿señal de squeeze o escasez genuina?)
- ¿Contango excesivo? (¿oportunidad de cash-and-carry?)

### 6. Implicaciones para hedging
- Para productores: ¿vender forward atractivo? (backwardation = peor precio forward)
- Para consumidores: ¿comprar forward atractivo? (contango = precio forward más alto)
- ¿Cambia la estrategia óptima de roll?

### 7. Consistencia con otros indicadores
- ¿La curva dice lo mismo que inventarios, premiums, y posicionamiento?
- Divergencias = oportunidad o señal de cambio inminente
