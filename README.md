# Cobre — Base de Conocimiento del Mercado del Cobre

Repositorio de conocimiento estructurado para el análisis del mercado del cobre,
diseñado para ser navegado tanto por humanos como por agentes AI.

## Qué es esto

Una base de conocimiento + pipeline de datos que cubre:
- **Fundamentos**: oferta, demanda, balance, costos, scrap, TC/RC
- **Pricing**: mecanismos de precio, curva forward, premiums, ratios cross-asset
- **Trading**: inventarios, flujos comerciales, posicionamiento especulativo
- **Derivados**: futuros, opciones, volatilidad, spreads, coberturas
- **Análisis técnico**: indicadores, estructura de mercado, señales
- **Macro**: ciclos, China, transición energética, geopolítica
- **ESG**: frameworks, regulación, carbono
- **Skills**: procedimientos analíticos reutilizables
- **Datos**: pipeline automatizado de datos cuantitativos con base DuckDB

## Cómo navegar

El archivo `indice.yaml` es el **grafo de conocimiento** central. Define cada documento
como un nodo con:
- `resumen`: qué contiene
- `tags`: temas que cubre
- `requiere`: documentos que hay que leer antes
- `alimenta`: documentos que usan este como input
- `relacionado`: documentos con temas que se solapan

Las **rutas** en el índice son secuencias predefinidas de nodos para análisis comunes
(evaluar una disrupción, analizar demanda china, diseñar cobertura, etc.).

## Pipeline de datos

El repo incluye un pipeline que descarga datos de mercado desde fuentes gratuitas
y los almacena en una base DuckDB local.

### Datos disponibles

| Fuente | Series | Frecuencia |
|---|---|---|
| Yahoo Finance | COMEX HG, DXY, Gold, US 10Y, S&P 500 | Diaria |
| Westmetall | LME Cash, LME 3M, LME stocks | Diaria |
| CFTC | COT managed money, producers, swap dealers | Semanal |
| FRED | Fed Funds Rate, Industrial Production, Trade Weighted USD | Diaria/Mensual |
| Calculado | COMEX-LME arb, LME Cash-3M spread, Cu/Au ratio | Diaria |

### Setup

```bash
# 1. Crear entorno virtual
python3 -m venv datos/.venv
datos/.venv/bin/pip install -r datos/requirements.txt

# 2. Configurar API keys
cp datos/.env.example datos/.env
# Editar datos/.env con tu FRED_API_KEY (gratis: https://fred.stlouisfed.org/docs/api/api_key.html)

# 3. Inicializar base de datos
datos/.venv/bin/python datos/scripts/init_db.py

# 4. Cargar datos
datos/.venv/bin/python datos/scripts/fetch_all.py            # últimos 30 días
datos/.venv/bin/python datos/scripts/fetch_all.py --backfill  # histórico completo
```

### Consultar datos

```python
import sys; sys.path.insert(0, "datos/scripts")
from db import query

query("SELECT * FROM clean.latest_prices")
query("SELECT report_date, managed_money_net FROM clean.cot ORDER BY report_date DESC LIMIT 5")
query("SELECT trade_date, value FROM clean.spreads WHERE spread_id = 'comex_lme_arb' ORDER BY trade_date DESC LIMIT 5")
```

Ver `datos/README.md` para documentación completa del pipeline, schema, y queries.

## Para agentes AI

Ver `CLAUDE.md` para instrucciones detalladas de navegación y uso del pipeline.
