# Cobre

Base de conocimiento estructurada del mercado del cobre, diseñada para ser
navegada por un asistente AI. Cargala en Claude, ChatGPT, o cualquier LLM
con acceso a archivos y obtené un analista de commodities que entiende
fundamentos, pricing, derivados, posicionamiento, y macro.

## Quick start

```bash
git clone https://github.com/nicorivas/cobre.git
cd cobre

# Setup del pipeline de datos (opcional pero recomendado)
python3 -m venv datos/.venv
datos/.venv/bin/pip install -r datos/requirements.txt
cp datos/.env.example datos/.env   # agregar FRED_API_KEY (gratis, opcional)
datos/.venv/bin/python datos/scripts/init_db.py
datos/.venv/bin/python datos/scripts/fetch_all.py
```

Luego abrí el repo en tu asistente AI favorito. El archivo `CLAUDE.md` contiene
las instrucciones que el agente necesita para navegar el grafo de conocimiento,
ejecutar skills, y consultar datos.

## Qué hay adentro

### Conocimiento (35 documentos interconectados)

| Dominio | Temas |
|---|---|
| **Fundamentos** | Oferta, demanda, balance, cost curves, scrap, TC/RC |
| **Pricing** | Mecanismos de precio, curva forward, premiums, cross-asset |
| **Trading** | Inventarios, flujos comerciales, posicionamiento, estacionalidad |
| **Derivados** | Futuros, opciones, volatilidad, spreads, coberturas |
| **Técnico** | Indicadores, estructura de mercado, señales combinadas |
| **Macro** | Ciclos, China, transición energética, geopolítica |
| **ESG** | Frameworks, regulación, carbono, impacto en mercado |

Cada documento es un nodo en un grafo definido en `indice.yaml`, con relaciones
explícitas (`requiere`, `alimenta`, `relacionado`) y rutas predefinidas para
análisis comunes.

### Datos cuantitativos

Pipeline Python que descarga datos de mercado a una base DuckDB local:

| Fuente | Series | Frecuencia |
|---|---|---|
| Yahoo Finance | COMEX HG, DXY, Gold, US 10Y, S&P 500, USD/CNY | Diaria |
| Westmetall | LME Cash, LME 3M, LME stocks | Diaria |
| SHFE | Precios Cu, inventarios, posicionamiento top 20 | Diaria |
| CFTC | COT managed money, producers, swap dealers | Semanal |
| FRED | Fed Funds Rate, Industrial Production | Diaria/Mensual |
| Calculado | COMEX-LME arb, LME-SHFE arb, LME Cash-3M, Cu/Au ratio | Diaria |

Ver `datos/README.md` para documentación completa del pipeline.

### Skills

Los skills son procedimientos analíticos que el asistente ejecuta paso a paso.
Cada uno define qué contexto cargar, qué datos consultar, y qué formato de
output producir.

| Skill | Qué hace |
|---|---|
| `analisis-semanal` | Revisión semanal completa del mercado |
| `analisis-posicionamiento` | Analizar COT semanal y señales contrarian |
| `analisis-tecnico` | Evaluar niveles técnicos y señales |
| `analisis-spreads` | Analizar spreads inter/intra-market |
| `analisis-curva-forward` | Interpretar estructura de término |
| `analisis-volatilidad` | Evaluar superficie de vol y régimen |
| `analisis-cost-curve` | Precio actual vs curva de costos |
| `analisis-tcrc` | Analizar mercado de TC/RC y concentrados |
| `interpretar-inventarios` | Interpretar movimientos de stocks LME/COMEX/SHFE |
| `monitor-china` | Evaluar impacto de noticias o datos chinos |
| `evaluar-proyecto-minero` | Evaluar viabilidad de proyecto de cobre |
| `evaluar-impacto-esg` | Evaluar impacto ESG en mercado u operación |
| `procesar-noticia` | Procesar noticia y actualizar temas activos |
| `resumir-paper` | Resumir paper/reporte y catalogar en referencias |
| `actualizar-temas-activos` | Revisar y actualizar narrativa de mercado |
| `init` | Orientarse: estado de datos, temas activos, sugerir siguiente paso |

Para ejecutar un skill, simplemente pedilo: *"hazme el análisis semanal"*,
*"procesa esta noticia: [texto]"*, *"¿cómo está el posicionamiento?"*.

## Cómo funciona

```
indice.yaml         →  Grafo de conocimiento (leer primero)
  ├── nodos         →  35 documentos con metadata, tags, conexiones
  └── rutas         →  9 secuencias predefinidas para análisis comunes

skills/             →  Procedimientos analíticos (el asistente los ejecuta)
datos/scripts/      →  Pipeline de datos (fetch → DuckDB → query)
CLAUDE.md           →  Instrucciones para el agente AI
```

El agente lee `indice.yaml`, identifica qué nodos son relevantes para tu
pregunta (por ruta predefinida o por tags), carga solo esos documentos,
y sigue el procedimiento del skill correspondiente. Si necesita datos
cuantitativos, consulta la base DuckDB via `datos/scripts/db.py`.

## Extender

**Agregar un documento**: crear el .md con front matter, agregar el nodo
a `indice.yaml` con tags y conexiones, actualizar nodos relacionados.

**Agregar una fuente de datos**: crear `datos/scripts/fetch_*.py` siguiendo
el patrón existente (ingest raw → upsert clean), agregar al orquestador
`fetch_all.py`.

**Agregar un skill**: crear `skills/nombre.md` con front matter (nombre,
descripcion, inputs, outputs) y procedimiento numerado. Referenciar los
nodos de contexto del `indice.yaml`.

## Limitaciones

- Esto es una **base de conocimiento**, no un sistema de trading. No genera
  señales de compra/venta ni ejecuta órdenes.
- Los datos del pipeline son **gratuitos y delayed**. No reemplaza un
  terminal Bloomberg ni un feed en tiempo real.
- El contenido refleja un punto de vista informado pero no es asesoría
  financiera. Verificá siempre los datos contra fuentes primarias.
- SHFE puede ser lento desde fuera de China (~60s por request).

## Licencia

MIT. Ver [LICENSE](LICENSE).
