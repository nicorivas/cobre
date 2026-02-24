---
nodo: trading/inventarios
---

# Inventarios de Cobre

## Por qué importan

Los niveles de inventario son el vínculo directo entre fundamentos (balance) y precio.
La relación inventarios-precio es la más importante del mercado.

## Inventarios visibles

### LME Warehouse Stocks

- Publicados diariamente por la LME (gratis)
- Ubicaciones: ~30 locations globales (Rotterdam, Busan, New Orleans, etc.)
- Desagregación clave:
  - **On-warrant**: metal disponible para entrega contra contratos (= stock verdadero)
  - **Cancelled warrants**: metal reservado para retiro físico (señal leading de drawdowns)
  - **Total**: on-warrant + cancelled warrants

| Nivel (total) | Señal histórica |
|---|---|
| > 500 kt | Mercado en surplus claro |
| 200-500 kt | Zona neutral |
| 100-200 kt | Tightness |
| < 100 kt | Escasez crítica, backwardation probable |

**Cancelled warrants como leading indicator**: un spike en cancelled warrants anticipa retiro físico en los próximos días/semanas.

### COMEX Stocks (Registered + Eligible)

- **Registered**: metal elegible para entrega contra contratos COMEX
- **Eligible**: en warehouse aprobado pero no registrado para entrega
- Publicados diariamente por CME
- Históricamente mucho menores que LME (EE.UU. no es hub de almacenamiento)
- En 2025: aumentaron dramáticamente (~650 kt entraron a EE.UU.) por tariff arbitrage

### SHFE Stocks

- Publicados semanalmente (viernes)
- Metal en warehouses designados por SHFE en China
- Alta estacionalidad: suben en Q1 (acumulación pre-Año Nuevo), bajan Q2-Q3

## Inventarios invisibles

Los stocks visibles (LME+COMEX+SHFE) representan solo **15-20% del inventario total** estimado.

### Inventarios no reportados

| Tipo | Estimación | Dificultad |
|---|---|---|
| Bonded warehouses China | 200-600 kt (varía) | Poco transparente; estimado por consultoras |
| SRB (State Reserve Bureau) | ~2 Mt (?) | Cifras oficiales no publicadas |
| Trader inventories | Desconocido | En tránsito, en warehouses privados |
| Pipeline inventory | ~2-3 semanas de consumo | Necesario para operaciones |

### El problema de los inventarios invisibles

- El balance oficial (ICSG) acumula un "statistical discrepancy"
- Un surplus acumulado que no se ve en stocks visibles implica que está en stocks invisibles
- Las estimaciones de inventarios invisibles pueden cambiar el narrativo de surplus a déficit
- China es el mayor punto ciego: bonded + SRB + trader stocks = potencialmente >1 Mt no reportado

## Days of coverage

```
Days of coverage = Inventarios visibles / (Consumo diario global)
                 = ~300 kt / (~72 kt/día) ≈ 4 días (visibles solamente)
```

Con invisibles estimados: posiblemente 15-25 días de coverage total.

Cuando days of coverage visible cae por debajo de ~3 días → alta probabilidad de backwardation y volatilidad.

## Relación inventarios-precio

La relación es **no lineal**:

```
Precio
  |        *
  |       *
  |      *
  |    *
  |  *
  | *
  |*
  |* * * * * * * *
  |_________________________
         Inventarios
```

- Cuando inventarios son altos: sensibilidad baja (cambio de 50kt apenas mueve precio)
- Cuando inventarios son bajos: sensibilidad alta (cambio de 50kt puede mover cientos de USD/t)
- JPMorgan: cuando LME on-warrant < 100kt, cobre sube 57% de las semanas con mediana +0.64%/semana
