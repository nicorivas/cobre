---
nodo: fundamentos/cost-curves
---

# Curvas de Costo del Cobre

## Definiciones de costo

### C1 (Cash Cost)
- Costo directo de producir una libra/tonelada de cobre pagable
- Incluye: minería, procesamiento, transporte, administración de sitio, TC/RC, royalties
- **Excluye**: depreciación, intereses, impuestos sobre renta
- Neto de **by-product credits** (oro, plata, molibdeno, ácido sulfúrico)
- Es la métrica más usada para comparar operaciones

### C2 (Producción total)
- C1 + depreciación y amortización
- Mejor proxy del costo económico de producción

### C3 (Costo total)
- C2 + intereses y costos corporativos
- Costo "fully loaded" incluyendo costo de capital

### AISC (All-In Sustaining Cost)
- C1 + sustaining capex + exploración + costos corporativos
- Métrica más conservadora, similar a C3 pero con sustaining capex explícito

## La curva de costos

Cuando se ordena toda la producción global de menor a mayor costo (C1):

```
Costo
(USD/lb)
 |
 |                                              ___/
 |                                         ___/
 |                                    ___/
 |                              ____/
 |                      _____/
 |             _______/
 |    ________/
 |___/
 |_____________________________________________
                                         Producción acumulada (Mt)
```

### Percentiles clave (~2024)

| Percentil | C1 aproximado (USD/lb) | Significado |
|---|---|---|
| 10th | ~$1.20-1.50 | Productores de muy bajo costo |
| 25th (Q1) | ~$1.50-1.80 | Primer cuartil |
| 50th (mediana) | ~$2.00-2.30 | Costo mediano |
| 75th (Q3) | ~$2.80-3.20 | Tercer cuartil |
| 90th | ~$3.50-4.00 | Productor marginal |

*Nota: estos rangos se actualizan con inflación de costos, leyes, FX, y by-product prices*

## Productor marginal como price floor

- En teoría, el precio no puede sostenerse por debajo del costo del productor marginal (90th percentil) por mucho tiempo
- Si precio < C1 del marginal → cierre de producción → oferta cae → precio sube
- En la práctica, hay inercia: minas operan con pérdida 6-18 meses antes de cerrar

## Variables que mueven la curva

| Factor | Efecto en la curva |
|---|---|
| Inflación de costos (energía, labor) | Sube toda la curva |
| Depreciación de moneda local (CLP, PEN, ZAR) | Baja la curva en USD |
| Caída de by-product prices (Au, Mo) | Sube la curva (menos créditos) |
| Declive de leyes de mineral | Sube la parte derecha de la curva |
| Nuevos proyectos de bajo costo | Aplana la parte izquierda |

## By-product credits

Pueden representar 10-40% de los costos para algunas minas:

| By-product | Minas beneficiadas | Impacto típico en C1 |
|---|---|---|
| Oro | Grasberg, Olympic Dam | -$0.20 a -$0.50/lb |
| Molibdeno | Collahuasi, El Teniente | -$0.10 a -$0.30/lb |
| Plata | KGHM, Antamina | -$0.05 a -$0.15/lb |
| Ácido sulfúrico | Smelters integrados | -$0.05 a -$0.15/lb |

## Fuentes de datos

- **Wood Mackenzie**: Referencia de la industria, actualización trimestral, requiere suscripción
- **CRU**: Alternativa, también por suscripción
- **S&P Global**: Capital IQ, datos de costos por mina
- Proxies públicas: reportes anuales de empresas cotizadas publican C1 por operación
