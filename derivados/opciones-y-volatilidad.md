---
nodo: derivados/opciones-y-volatilidad
---

# Opciones y Volatilidad del Cobre

## Opciones sobre futuros de cobre

### COMEX Copper Options
- Subyacente: 1 contrato futuro de COMEX HG (25,000 lbs)
- Estilo: American (ejercicio antes de vencimiento)
- Strikes: cada $0.01/lb (~$220/t)
- Vencimientos: mensuales, algunos weekly

### LME Copper Options
- Subyacente: 1 lote LME (25 t)
- Estilo: Asian (promedio del pricing period) o European
- TAPOs (Traded Average Price Options): settleadas contra promedio mensual

## La superficie de volatilidad

La superficie de vol implícita tiene tres dimensiones:

### 1. Nivel de volatilidad (ATM IV)

La volatilidad implícita at-the-money indica la expectativa de magnitud de movimiento.

| IV anualizada | Contexto de mercado |
|---|---|
| < 15% | Muy baja: mercado complaciente, rango estrecho |
| 15-25% | Normal: rango habitual para cobre |
| 25-35% | Elevada: incertidumbre significativa |
| > 35% | Muy alta: crisis, eventos extremos, squeezes |

### 2. Skew (dimensión de strike)

La diferencia de IV entre strikes para un mismo vencimiento:

```
Skew = IV(25-delta put) - IV(25-delta call)
```

| Skew | Significado |
|---|---|
| **Positivo** (puts más caras) | Mercado quiere protección downside |
| **Negativo** (calls más caras) | Mercado teme upside risk (squeeze, supply shock) |
| **Neutral** | Sin sesgo direccional percibido |

Para cobre: el skew suele ser ligeramente positivo (más demanda de puts por hedging de productores), pero se invierte durante supply shocks.

### 3. Term structure de volatilidad (dimensión de tiempo)

```
Term structure = IV(largo plazo) - IV(corto plazo)
```

| Forma | Significado |
|---|---|
| **Normal** (upward: LP > CP) | Mercado espera volatilidad futura mayor que actual |
| **Invertida** (downward: CP > LP) | Evento inminente con vol alta, mercado espera normalización |
| **Flat** | Sin expectativas de cambio en régimen de vol |

## Greeks

| Greek | Mide | Importancia para cobre |
|---|---|---|
| **Delta** | Sensibilidad al precio del subyacente | Gestión de dirección |
| **Gamma** | Cambio de delta por movimiento de precio | Riesgo en eventos (gamma squeeze) |
| **Vega** | Sensibilidad a cambios de IV | Exposición a régimen de volatilidad |
| **Theta** | Decay temporal | Costo de carry de opciones |
| **Rho** | Sensibilidad a tasas | Menor importancia relativa |

## IV vs Realized Volatility

```
Vol premium = IV - Realized Vol
```

- **Vol premium positivo** (IV > RV): opciones "caras" → posible venta de vol
- **Vol premium negativo** (IV < RV): opciones "baratas" → posible compra de vol
- Históricamente: IV tiende a superar RV (risk premium por incertidumbre)

## Estrategias principales

### Coberturas

| Estrategia | Perfil | Uso |
|---|---|---|
| **Long put** | Protección downside ilimitada | Productores hedgeando |
| **Long call** | Protección upside ilimitada | Consumidores hedgeando |
| **Collar** (long put + short call) | Protección acotada, costo reducido | Productores; explota skew |
| **Put spread** | Protección parcial, costo bajo | Hedge parcial con presupuesto limitado |

### Trading de volatilidad

| Estrategia | View implícito |
|---|---|
| **Long straddle** | Vol va a subir; dirección incierta |
| **Short straddle** | Vol va a bajar; precio estable |
| **Calendar spread** | Term structure va a cambiar |
| **Risk reversal** | Skew va a cambiar |

## Eventos que mueven la vol

- Anuncios de tariffs/sanciones
- Datos macro sorpresivos (PMI, employment, PIB China)
- Disrupciones de oferta (huelgas, accidentes, clima)
- Decisiones de política monetaria (Fed, PBOC)
- LME Week (octubre): señales sobre outlook
