---
nodo: noticias/temas-activos
---

# Temas Activos del Mercado

*Última actualización: 2026-02-24*

Este archivo se actualiza cada vez que se procesa una noticia relevante.
Captura el narrativo dominante del mercado en cualquier momento.

## Temas activos

### Fallo SCOTUS contra tariffs IEEPA y reemplazo con Section 122

- **Status**: activo
- **Desde**: 2026-02-20
- **Impacto**: mixto
- **Magnitud**: alta
- **Nodos relacionados**: [macro/geopolitica, derivados/spreads, pricing/premiums-y-descuentos, trading/flujos-comerciales]
- **Resumen**: La Corte Suprema anuló (6-3) el uso de IEEPA para imponer tariffs. Trump reemplazó en horas con un tariff global de 10% bajo Section 122 del Trade Act de 1974, luego anunciado a 15%. Section 122 solo dura 150 días sin aprobación del Congreso. Los tariffs de cobre bajo Section 232 (50%) no fueron afectados — siguen vigentes. El impacto neto para cobre es limitado en lo directo, pero la incertidumbre regulatoria mueve el arb COMEX-LME y los flujos de metal.
- **Última actualización**: 2026-02-24 — mercado digiriendo la transición IEEPA → Section 122. Cobre subió +5.8% COMEX el lunes, pero por arrastre de rally broad de metales (oro +5.8% mismo día), no por driver específico de cobre.

### Cobre "económicamente atrapado" en EE.UU. — COMEX en máximos de 30 años

- **Status**: activo
- **Desde**: 2025 (aceleró H2 2025)
- **Impacto**: bearish para LME / bullish para COMEX premium
- **Magnitud**: alta
- **Nodos relacionados**: [trading/inventarios, derivados/spreads, derivados/microestructura, macro/geopolitica, trading/flujos-comerciales]
- **Resumen**: COMEX acumuló ~590,000 short tons (534 kt) — record desde 1989. Se estiman 700-830 kt "económicamente atrapadas" en EE.UU. por front-running de tariffs Section 232 (50%). El metal no sale porque el premium COMEX hace que exportar sea no rentable. Esto drena inventarios globales (LME cayó a <100 kt en dic-2025) y distorsiona el mercado en dos precios regionales distintos. Analistas lo llaman "The Great Copper Disconnect".
- **Última actualización**: 2026-02-24 — post fallo SCOTUS, parte del metal parece estar fluyendo de vuelta a LME. Inventarios LME subieron de 170 kt a 242 kt en un mes (+71 kt). El arb COMEX-LME oscila violentamente (-$449 a +$169 en febrero), reflejando repricing continuo del régimen tarifario.

### Build acelerado de inventarios LME

- **Status**: activo
- **Desde**: 2026-01-26
- **Impacto**: bearish (corto plazo)
- **Magnitud**: media-alta
- **Nodos relacionados**: [trading/inventarios, pricing/estructura-de-termino, derivados/microestructura]
- **Resumen**: LME stocks subieron de 170 kt a 242 kt en un mes (+42%). Semana del 17-23 feb: +30 kt, el mayor build semanal del dataset. El contango LME cash-3M se mantiene profundo (-$83, vs promedio 1Y de -$22). El build parece ser redireccionamiento de metal desde EE.UU./bonded China hacia LME, no surplus de producción. Si es transitorio, la señal bearish se debilita una vez que se estabilice.
- **Última actualización**: 2026-02-24 — ritmo de build aceleró a ~6,000 t/día en segunda mitad de semana. Monitorear si continúa o se frena.

### Rally de oro y safe-haven demand — Cu/Au en mínimos

- **Status**: activo
- **Desde**: 2026-01 (aceleró feb)
- **Impacto**: bearish relativo (cobre underperforma oro)
- **Magnitud**: media
- **Nodos relacionados**: [pricing/cross-asset, macro/indicadores-macro, macro/geopolitica]
- **Resumen**: Oro superó $5,400 en enero (ATH) impulsado por tensiones geopolíticas (Greenland, Iran), incertidumbre tarifaria, y safe-haven demand. Cu/Au ratio cayó a 1.11, mínimo del año (promedio 1Y: 1.37). Cobre sube por arrastre de metales pero no lidera — señal de que la demanda física de cobre no es el driver. Un Cu/Au bajo históricamente correlaciona con expectativas macro débiles.
- **Última actualización**: 2026-02-24 — oro +5.8% y cobre +5.8% en COMEX el mismo día, pero Cu/Au sigue comprimiéndose porque oro subió desde base más alta.

### Section 232 cobre (50%) y decisión de tariff sobre cátodo refinado

- **Status**: en desarrollo
- **Desde**: 2025 (Section 232 implementado)
- **Impacto**: bullish COMEX / bearish resto del mundo
- **Magnitud**: alta
- **Nodos relacionados**: [macro/geopolitica, trading/flujos-comerciales, derivados/spreads, pricing/premiums-y-descuentos]
- **Resumen**: Section 232 impone 50% sobre productos de cobre semi-terminados. Queda pendiente la decisión sobre cobre refinado (cátodo): update el 30 de junio 2026 para evaluar un tariff escalonado — 15% desde enero 2027, subiendo a 30% en 2028. Si se implementa, el premium COMEX se ampliaría aún más y el metal atrapado en EE.UU. crecería. Esta es la decisión regulatoria más importante para cobre en 2026.
- **Última actualización**: 2026-02-24 — sin cambios post-SCOTUS; Section 232 no fue afectado por el fallo.

## Formato de un tema activo

```
### [Nombre del tema]

- **Status**: activo / en desarrollo / resuelto
- **Desde**: fecha de inicio
- **Impacto**: bullish / bearish / neutral / incierto
- **Magnitud**: alta / media / baja
- **Nodos relacionados**: [lista de nodos del indice.yaml relevantes]
- **Resumen**: descripción breve del tema y su estado actual
- **Última actualización**: fecha y descripción del último desarrollo
```
