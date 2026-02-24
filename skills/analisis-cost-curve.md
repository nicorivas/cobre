---
nombre: analisis-cost-curve
descripcion: Evaluar el nivel de precio actual contra la curva de costos
nodos:
  - fundamentos/cost-curves
  - fundamentos/oferta
  - pricing/mecanismos-de-precio
contexto_condicional:
  - si: precio_cerca_de_marginal
    agregar: [macro/ciclos-y-superciclos]
inputs:
  - precio actual del cobre
  - datos de cost curve si disponibles (o usar estimaciones del nodo)
outputs:
  - posición del precio en la curva
  - sostenibilidad del nivel actual
  - riesgo de cierre de minas o incentivo para nuevos proyectos
---

# Skill: Análisis de Cost Curve

## Procedimiento

### 1. Precio actual vs percentiles
- Convertir precio actual a USD/lb si necesario
- ¿Dónde cae en la curva? (< Q1, Q1-mediana, mediana-Q3, > Q3, > 90th)
- Referencia rápida: comparar con C1 estimates del nodo fundamentos/cost-curves

### 2. Sostenibilidad
- **Precio > 90th percentil**: toda la industria es rentable; incentiva nueva capacidad
- **Precio entre mediana y 90th**: mayoría rentable; status quo
- **Precio entre 25th y mediana**: presión sobre productores de alto costo
- **Precio < 25th percentil**: muchos productores bajo agua; cierres probables

### 3. Price floor implícito
- El 90th percentil C1 (~$3.50-4.00/lb en 2024) es el price floor teórico
- En la práctica, hay inercia: precio puede estar bajo el 90th por 6-18 meses
- Pero no indefinidamente: cierres de minas eventualmente soportan el precio

### 4. Incentive price
- Precio necesario para justificar nuevo greenfield capex
- Generalmente > $4.00-4.50/lb (C3 + retorno sobre capital)
- Si precio actual < incentive price → pipeline de proyectos se contrae → bullish LP

### 5. Factores que mueven la curva
- ¿Cambió el USD recientemente? (depreciación de CLP/PEN baja la curva en USD)
- ¿Cambió el precio de by-products? (Au, Mo, Ag afectan C1)
- ¿Inflación de costos? (energía, labor, consumibles)
- ¿Leyes de mineral en declive? (sube la parte derecha de la curva)

### 6. Implicaciones
- ¿El precio actual es sostenible por fundamentales? ¿O necesita corrección?
- ¿Qué productores están en riesgo de cierre/recorte?
- ¿Qué proyectos nuevos se justifican al precio actual?
