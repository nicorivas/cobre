---
nodo: pricing/estructura-de-termino
---

# Estructura de Término del Cobre

## Conceptos fundamentales

### Contango
- Precio forward > precio spot
- Curva inclinada hacia arriba
- Señal: oferta spot adecuada, costo de carry positivo
- Roll yield: **negativo** (pagar para mantener posición larga)

### Backwardation
- Precio spot > precio forward
- Curva inclinada hacia abajo
- Señal: escasez inmediata, demanda urgente de metal físico
- Roll yield: **positivo** (cobrar por mantener posición larga)

## Theory of Storage

El precio forward se descompone en:

```
F(T) = S × e^{(r + w - y) × T}

Donde:
  S = precio spot
  r = tasa de interés libre de riesgo (cost of capital)
  w = costo de almacenamiento (warehouse rent, seguro)
  y = convenience yield (beneficio de tener metal físico)
```

### Convenience yield
- Beneficio implícito de tener inventario físico disponible
- **Inversamente proporcional** a los niveles de inventario (relación no lineal)
- Cuando inventarios son bajos → convenience yield alta → backwardation
- Cuando inventarios son altos → convenience yield baja → contango

## Cash-to-3-Month spread (LME)

El spread más monitoreado del mercado:

| Nivel | Nombre | Significado |
|---|---|---|
| > 0 (cash > 3M) | Backwardation | Escasez spot; urgencia por metal |
| = 0 | Flat | Equilibrio |
| < 0 (cash < 3M) | Contango | Oferta spot adecuada; metal disponible |
| >> 0 (extremo) | Super backwardation | Squeeze o escasez crítica |

### Señales históricas
- Backwardation sostenida >$50/t: generalmente asociada a inventarios LME < 200kt
- Super back >$200/t: eventos de squeeze (raro pero impactante)
- Contango >$50/t: inventarios altos, mercado en surplus claro

## Roll yield

Para un inversionista con posición larga en futuros:

```
Roll yield mensual ≈ (F_near - F_far) / F_far × (30/días entre contratos)
```

| Estructura | Roll yield | Implicación para longs |
|---|---|---|
| Contango | Negativo | Erosiona retornos (~2-5% anual en contango normal) |
| Backwardation | Positivo | Mejora retornos (puede ser significativo >5% anual) |

## Curva forward completa

La curva LME tiene precios diarios hasta 3M, semanales 3-6M, mensuales hasta 10Y.
La mayoría de la liquidez se concentra en los primeros 15 meses.

Formas de la curva:
- **Normal contango**: gently upward sloping (lo más común históricamente)
- **Backwardation front**: cash/nearby en back, deferred en contango
- **Full backwardation**: toda la curva invertida (escasez prolongada esperada)
- **Humped**: pico en un punto medio (e.g., por estacionalidad)

## Relación con inventarios

La relación inventarios-estructura de término es el corazón del análisis:

```
Inventarios altos → convenience yield baja → contango
Inventarios bajos → convenience yield alta → backwardation
```

Esta relación es no lineal: la sensibilidad del spread a cambios en inventarios aumenta
dramáticamente cuando los inventarios están por debajo de cierto umbral.
