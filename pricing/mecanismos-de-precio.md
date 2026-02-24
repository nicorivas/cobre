---
nodo: pricing/mecanismos-de-precio
---

# Mecanismos de Precio del Cobre

## Las tres bolsas principales

### LME (London Metal Exchange)
- **Dominante** en price discovery global
- Contrato principal: LME Copper Grade A (lot = 25 t)
- Vencimientos: daily out to 3 months, weekly 3-6M, monthly 6M-10Y
- Sesiones: Ring (open outcry, 2 sesiones de 5 min), Kerb, LME Select (electrónico)
- **Official Price**: fijado al cierre del segundo Ring (12:30-12:35 GMT)
- Settlement: T+2 para cash, prompt date para forward
- Entrega física en warehouses LME autorizados (~500+ warehouses, ~30 ubicaciones)

### COMEX (CME Group)
- Contrato: HG Copper (lot = 25,000 lbs ≈ 11.34 t)
- Cotiza en centavos/libra (convertir: ×22.0462 = USD/t)
- Vencimientos mensuales, mayor liquidez en meses pares
- Predominantemente electrónico (Globex)
- Entrega en COMEX-approved warehouses (EE.UU.)
- Mayor participación de financial players vs LME

### SHFE (Shanghai Futures Exchange)
- Contrato: CU (lot = 5 t)
- Cotiza en RMB/t
- Acceso restringido a participantes domésticos (excepto vía Shanghai INE)
- Refleja condiciones del mercado chino (precio = LME + premium + VAT)
- Horario de trading incluye sesión nocturna

## Jerarquía de price discovery

Investigaciones empíricas muestran consistentemente:

```
LME → lidera → COMEX y SHFE siguen
```

- LME domina en lead-lag, volatility spillover, y transmisión de información
- SHFE tiene spillover creciente sobre LME en ciertas condiciones
- COMEX gana importancia en eventos US-specific (tariffs, datos macro)

## Pricing de contratos físicos

Los contratos físicos de cobre refinado NO se cotizan a precio fijo. Usan:

```
Precio = Base LME (o COMEX) + Premium/Descuento
```

### Pricing periods
- **QP (Quotational Period)**: mes(es) del cual se toma el promedio LME
- Típicamente: M+1, M+2, o promedio del mes de embarque
- El comprador o vendedor puede tener opción de "pricing" (elegir días dentro del QP)

### Pricing de concentrado
- Base: promedio LME del QP acordado
- Menos: TC/RC
- Más/menos: ajustes por calidad, impurezas, subproductos

## Conversiones útiles

| De | A | Factor |
|---|---|---|
| USD/lb | USD/t | × 2,204.62 |
| USD/t | USD/lb | ÷ 2,204.62 |
| RMB/t | USD/t | ÷ tipo de cambio USDCNY |
| COMEX cents/lb | USD/t | × 22.0462 |
