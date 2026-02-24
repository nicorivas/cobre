---
nodo: derivados/futuros-y-forwards
---

# Futuros y Forwards de Cobre

## Contratos de futuros en bolsa

### COMEX HG Copper (CME Group)

| Característica | Detalle |
|---|---|
| Tamaño del contrato | 25,000 lbs (~11.34 t) |
| Cotización | Centavos/lb |
| Tick mínimo | 0.0005 $/lb ($12.50/contrato) |
| Meses de vencimiento | Todos los meses (mayor liquidez en meses pares) |
| Settlement | Entrega física en warehouses aprobados |
| Margen inicial | ~$6,000-10,000/contrato (varía) |
| Horario | Casi 24h (Globex): domingo 17:00 - viernes 16:00 CT |

### LME Copper Grade A

| Característica | Detalle |
|---|---|
| Tamaño del lote | 25 toneladas métricas |
| Cotización | USD/t |
| Tick mínimo | $0.50/t ($12.50/lote) |
| Prompt dates | Diarios hasta 3M, semanales 3-6M, mensuales 6M+ (hasta 123M) |
| Settlement | Entrega física en LME-approved warehouses |
| Margen | Set por LME Clear; ~$5,000-8,000/lot |
| Particularidad | Prompt date system (no meses fijos como COMEX) |

### SHFE Copper (CU)

| Característica | Detalle |
|---|---|
| Tamaño del contrato | 5 toneladas |
| Cotización | RMB/t |
| Meses | Mensuales (12 meses forward) |
| Settlement | Entrega en warehouses SHFE en China |
| Acceso | Restringido a participantes domésticos (o vía INE) |

## OTC Forwards y Swaps

- **Forwards**: contratos bilaterales, customizables en tenor y cantidad
- **Swaps**: acuerdo para intercambiar precio fijo por precio flotante (promedio LME de un período)
- Mayor flexibilidad que futuros en bolsa pero con riesgo de contraparte
- Clearing: algunos swaps se clearean vía LME Clear o CME

## Roll mechanics

### Qué es el roll
Al acercarse el vencimiento, una posición en futuros debe "rollarse" al siguiente contrato:
1. Cerrar (vender) el contrato que vence
2. Abrir (comprar) el contrato del siguiente período

### Costo del roll

```
Costo de roll = Precio del contrato nuevo - Precio del contrato que vence
```

- En **contango**: costo positivo (comprar más caro, vender más barato) → roll cost
- En **backwardation**: costo negativo (comprar más barato, vender más caro) → roll yield

### Estrategias de roll
- **Calendar roll**: roll estándar al siguiente mes/prompt
- **Optimized roll**: elegir el contrato más eficiente en la curva (no necesariamente el próximo)
- **Pre-roll**: ejecutar antes del período de mayor actividad de roll (evitar crowding)

## Liquidez

### COMEX
- Front month: mayor liquidez, >100k contratos OI típico
- 2nd-3rd month: buena liquidez
- Back months: liquidez decreciente

### LME
- 3-month: mayor liquidez
- Cash: segunda mayor liquidez
- Forward months: decreciente pero funcional hasta ~15 meses

### Implicaciones
- Spreads bid-ask más amplios en contratos menos líquidos
- Slippage mayor para posiciones grandes en back months
- El calendar spread entre meses líquidos tiene tighter spreads
