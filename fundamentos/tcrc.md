---
nodo: fundamentos/tcrc
---

# TC/RC — Treatment Charges y Refining Charges

## Qué son

Los TC/RC son los pagos que el minero hace al smelter/refiner por procesar concentrado:

- **TC (Treatment Charge)**: USD por tonelada métrica seca (dmt) de concentrado
- **RC (Refining Charge)**: centavos USD por libra de cobre pagable

Son la principal fuente de ingresos de las fundiciones/refinerías custom (no integradas).

## Fórmula de precio del concentrado

```
Precio del concentrado (por dmt) =
  (Contenido de Cu pagable × Precio LME) - TC - (Contenido de Cu pagable × RC)
  + Créditos por subproductos (Au, Ag)
  - Penalidades por impurezas (As, Hg, F)
```

Ejemplo simplificado:
- Concentrado de 30% Cu, TC = $80/dmt, RC = $0.08/lb
- Si LME = $9,000/t, Cu pagable = 0.30 × 1,000 kg × ($9.00/kg - $0.18/kg) - $80 = $2,566/dmt

## Benchmark anual vs spot

### Benchmark anual
- Negociado entre los mayores productores (Freeport, BHP, Antofagasta) y los mayores smelters (chinos)
- Se fija al inicio de cada año para el año calendario
- Referencia para la mayoría de contratos de largo plazo
- 2024 benchmark: $80/t y $0.08/lb (significativamente bajo)
- 2025 benchmark: no logró fijarse inicialmente por condiciones extremas

### TC/RC spot
- Negociado semanalmente en el mercado spot
- Más volátil que el benchmark
- En 2025 cayó a territorio negativo (< $0/dmt) → smelters pagando a mineros

## Como indicador de mercado

| TC/RC | Señal | Implicaciones |
|---|---|---|
| **Altos** (>$80/dmt) | Abundancia de concentrado vs capacidad de fundición | Smelters en posición fuerte; mercado minero en surplus |
| **Medios** ($40-80/dmt) | Mercado equilibrado | — |
| **Bajos** (<$40/dmt) | Escasez de concentrado | Mineros en posición fuerte; presión sobre márgenes de smelters |
| **Negativos** | Escasez extrema | Smelters compiten por concentrado hasta perder dinero |

## TC/RC negativos en 2025

La situación extrema de 2025 refleja:
- Crecimiento de capacidad de fundición (especialmente China e Indonesia) superando el crecimiento de producción mina
- Disrupciones en producción mina (Cobre Panamá cerrada, problemas en Chile)
- Resultado: smelters chinos operando a pérdida, algunos recortando producción

## Efecto cascada de TC/RC bajos

1. TC/RC cae → márgenes de smelters se comprimen
2. Smelters recortan producción de refinado
3. Oferta de refinado cae → déficit de refinado se amplía
4. Precio del cátodo sube
5. Mineros se benefician doblemente: precio alto + TC/RC bajo

## Fuentes de datos

- **Fastmarkets**: TC/RC spot semanal (referencia del mercado)
- **CRU**: TC/RC spot y análisis
- **SMM**: TC/RC para mercado chino
- **Benchmark anual**: anunciado públicamente cuando se acuerda
