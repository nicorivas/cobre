---
nodo: derivados/microestructura
---

# Microestructura del Mercado de Derivados de Cobre

## LME Warehouse System

### Estructura

```
Metal entra → Warehouse LME → Warrant emitido → Tradeable en LME → Cancelled → Metal sale
```

### Conceptos clave

| Concepto | Definición |
|---|---|
| **Warrant** | Título de propiedad de un lote de 25t en un warehouse LME |
| **On-warrant** | Metal con warrant vigente, disponible para entrega contra contratos |
| **Cancelled warrant** | Warrant cancelado; metal reservado para retiro físico |
| **Live warrant** | Sinónimo de on-warrant |
| **Rent** | Costo diario de almacenamiento (~$0.50-0.80/t/día) |
| **Load-out rate** | Velocidad mínima de salida de metal del warehouse (t/día) |

### Cancelled warrants como señal

```
Cancelled warrants altos → metal va a salir → stocks van a caer → bullish
```

- Un spike en cancelled warrants anticipa caída de stocks en días/semanas
- En 2025: 50,000t canceladas en un solo día → señal extrema de tightness

### Queue dynamics

- Si muchos quieren retirar metal → se forma cola (queue) en el warehouse
- LME tiene reglas de load-out rate mínimo (e.g., 3,000 t/día para warehouses grandes)
- Queues largas significan que el metal cancelado tarda semanas/meses en salir
- Históricamente un problema en ciertos locations (Detroit pre-2014)

### Warehouse location dynamics

No todo el metal LME es igual — la ubicación importa:

| Location | Relevancia |
|---|---|
| Rotterdam/Vlissingen | Hub europeo; cerca de consumidores EU |
| Busan | Hub asiático ex-China |
| New Orleans | Hub americano (pre-tariffs) |
| Kaohsiung | Taiwan, hub de tránsito |
| Port Klang | Malaysia |

La distribución de stocks por location afecta premiums regionales y logística de entrega.

## COMEX Warehouse System

### Categorías de inventario

| Categoría | Definición |
|---|---|
| **Registered** | Metal registrado para entrega contra contratos COMEX |
| **Eligible** | Metal en warehouse aprobado, cumple specs, pero NO registrado |
| **Total** | Registered + Eligible |

Nota: el movimiento de eligible a registered (o viceversa) puede señalar
intención de entrega o retiro del mercado entregable.

### Warehouses COMEX

- Ubicados en EE.UU. (Arizona, Utah, Illinois, New York)
- Menor red que LME pero expandida en 2025 por el inflow de metal

## Squeezes

### Qué es un squeeze
Cuando un participante (o grupo) acumula una posición dominante en:
- Warrants (controla el metal disponible para entrega)
- Futuros corto plazo (controla la demanda de entrega)

Resultado: backwardation extrema, precios spot se disparan, shorts forzados a cubrir a precios elevados.

### Indicadores de riesgo de squeeze
- Un solo holder con >40% del inventario on-warrant (LME publica lending guidance cuando esto ocurre)
- Cancelled warrants > 50% del total
- Open interest nearby > on-warrant stocks
- Backwardation ampliándose rápidamente

### Regulación anti-squeeze
- LME: reglas de position accountability, lending guidance (obligación de prestar warrants)
- COMEX: position limits, large trader reporting
- Históricamente: Sumitomo scandal (1996), Hamanaka acumuló posición dominante
