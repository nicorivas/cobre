---
nombre: analisis-tcrc
descripcion: Analizar el mercado de TC/RC y sus implicaciones
nodos:
  - fundamentos/tcrc
  - fundamentos/oferta
  - fundamentos/balance-de-mercado
contexto_condicional:
  - si: tc_negativo
    agregar: [macro/china]
  - si: cambio_benchmark
    agregar: [fundamentos/cost-curves]
inputs:
  - TC/RC spot actual y cambio reciente
  - contexto (¿por qué cambió?)
outputs:
  - interpretación del nivel de TC/RC
  - implicaciones para balance de refinado y precio
---

# Skill: Análisis de TC/RC

## Procedimiento

### 1. Nivel actual
- TC spot actual (USD/dmt) y RC (c/lb)
- Comparar con benchmark anual vigente
- Comparar con rango histórico (5 años)
- ¿En zona alta, media, baja, o negativa?

### 2. Tendencia
- ¿TC/RC subiendo o bajando? ¿Desde cuándo?
- Velocidad del cambio (gradual o brusco)

### 3. Diagnóstico del mercado de concentrados
- TC/RC altos → concentrado abundante vs capacidad de fundición
- TC/RC bajos → concentrado escaso vs capacidad
- TC/RC negativos → smelters compitiendo desesperadamente por feed

### 4. Causas
- **Supply side**: ¿producción mina creció/cayó? ¿Disrupciones?
- **Demand side**: ¿nueva capacidad de fundición? ¿Cierres de smelters?
- ¿Factores temporales (mantenimiento) o estructurales?

### 5. Implicaciones para smelters
- Con TC/RC actual, ¿smelters son rentables?
- Si no → ¿recortes de producción de refinado probables?
- ¿Cuánto tiempo pueden operar a pérdida? (inercia de 3-6 meses típico)

### 6. Cascada al mercado de refinado
- Recortes de smelter → menos oferta de refinado → bullish para cátodo
- Expansión de smelter → más oferta de refinado → bearish para cátodo
- ¿El balance de refinado cambia materialmente?

### 7. Señal para precio del cobre
- TC/RC muy bajos + inventarios bajos = señal alcista fuerte
- TC/RC altos + inventarios altos = señal bajista
- TC/RC bajos pero inventarios altos = señal mixta (problema de concentrado pero no de refinado)
