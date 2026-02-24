---
nombre: interpretar-inventarios
descripcion: Interpretar movimientos de inventarios y sus implicaciones
nodos:
  - trading/inventarios
  - pricing/estructura-de-termino
  - derivados/microestructura
  - fundamentos/balance-de-mercado
contexto_condicional:
  - si: movimiento_en_LME
    agregar: [derivados/microestructura]
  - si: movimiento_en_SHFE
    agregar: [macro/china]
  - si: movimiento_en_COMEX
    agregar: [macro/geopolitica, derivados/spreads]
inputs:
  - datos de inventarios (qué cambió, cuánto, dónde)
outputs:
  - interpretación del movimiento
  - implicaciones para precio y estructura de término
---

# Skill: Interpretar Inventarios

## Procedimiento

### 1. Identificar el movimiento
- ¿Qué bolsa? (LME, COMEX, SHFE)
- ¿Magnitud? (comparar con promedio diario/semanal)
- ¿Dirección? (build o draw)

### 2. Descomponer (LME)
- ¿El cambio fue en on-warrant, cancelled warrants, o ambos?
- Si cancelled warrants subieron: metal va a salir → draw próximo
- Si on-warrant subió: nuevo metal entrando → build
- ¿En qué warehouse/location?

### 3. Descomponer (COMEX)
- ¿Cambio en registered o eligible?
- Movimiento de eligible → registered = intención de entrega
- Movimiento de registered → eligible = metal retirado del entregable

### 4. Contextualizar
- ¿El movimiento es consistente con el balance de mercado esperado?
- ¿Es estacional? (SHFE sube en Q1 normalmente)
- ¿Es un one-off (movimiento de un trader grande) o tendencia?
- Calcular days of coverage actualizados

### 5. Evaluar impacto en estructura de término
- ¿Inventarios cayendo → debería profundizar backwardation?
- ¿Inventarios subiendo → debería moderarse el back / ampliar contango?
- ¿El cash-3M spread se movió coherentemente?

### 6. Check de inventarios invisibles
- ¿Hay información sobre bonded stocks de China? (CRU/SMM estimates)
- ¿El movimiento visible puede estar compensado por movimiento invisible?
- ¿Hay flujos regionales explicando el movimiento? (metal moviéndose entre bolsas)

### 7. Implicaciones
- ¿Señal bullish, bearish, o neutral?
- ¿Requiere ajuste de view de mercado?
- ¿Alguna oportunidad de trading? (spread, outright)
