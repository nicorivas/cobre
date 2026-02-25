# datos/ — Pipeline de datos cuantitativos

Pipeline para descargar, normalizar y consultar datos del mercado del cobre.
Los datos se almacenan en DuckDB (archivo local, sin servidor).

## Setup

### 1. Crear entorno virtual e instalar dependencias

```bash
python3 -m venv datos/.venv
datos/.venv/bin/pip install -r datos/requirements.txt
```

### 2. Configurar API keys

Copiar el archivo de ejemplo y completar los valores:

```bash
cp datos/.env.example datos/.env
```

Editar `datos/.env`:

```
FRED_API_KEY=tu_key_aqui
```

#### Obtener FRED API Key (gratis)

1. Ir a https://fred.stlouisfed.org/docs/api/api_key.html
2. Crear cuenta (o usar cuenta existente de FRED)
3. Solicitar API key — se genera al instante
4. Copiar la key en `datos/.env`

> Sin FRED_API_KEY el pipeline funciona igual, pero se saltan los datos macro
> (Fed Funds Rate, ISM PMI, Trade Weighted USD).

### 3. Inicializar la base de datos

```bash
datos/.venv/bin/python datos/scripts/init_db.py
```

Esto crea `datos/cobre.duckdb` con el schema completo y el catálogo de series.

### 4. Cargar datos

```bash
# Datos recientes (últimos 30 días)
datos/.venv/bin/python datos/scripts/fetch_all.py

# Backfill completo (2 años precios, 3 años COT)
datos/.venv/bin/python datos/scripts/fetch_all.py --backfill
```

## Uso recurrente

```bash
# Actualización diaria/semanal — un solo comando
datos/.venv/bin/python datos/scripts/fetch_all.py
```

Es idempotente: correr dos veces no duplica datos en las tablas clean.

## Estructura

```
datos/
├── cobre.duckdb           ← base de datos (gitignored, se regenera)
├── schema.sql             ← DDL de todas las tablas y views
├── requirements.txt       ← dependencias Python
├── .env                   ← API keys (gitignored)
├── .env.example           ← template de configuración
├── seeds/
│   └── series_catalog.csv ← catálogo de series (28 definidas)
├── scripts/
│   ├── db.py              ← módulo core (connect, ingest, upsert, query)
│   ├── init_db.py         ← inicializa la DB desde schema.sql + seeds
│   ├── fetch_comex.py     ← COMEX HG, DXY, Gold, US 10Y, S&P 500, USD/CNY
│   ├── fetch_fred.py      ← Fed Funds, ISM PMI, Trade Weighted USD
│   ├── fetch_cot.py       ← CFTC COT managed money copper
│   ├── fetch_shfe.py      ← SHFE Cu precios, inventarios, posicionamiento top 20
│   ├── calc_spreads.py    ← spreads derivados (Cu/Au, COMEX-LME, LME-SHFE arb)
│   └── fetch_all.py       ← orquestador
└── queries/
    ├── snapshot_semanal.sql   ← para el skill analisis-semanal
    └── posicionamiento.sql    ← para el skill analisis-posicionamiento
```

## Schema de la base de datos

Tres capas:

| Schema | Propósito |
|---|---|
| `raw` | Datos inmutables tal como llegaron. Append-only. Audit trail. |
| `clean` | Datos normalizados, deduplicados, consultables. Upsert por clave natural. |
| `meta` | Catálogo de series y views de cobertura. |

Tablas principales en `clean`:

| Tabla | Clave primaria | Contenido |
|---|---|---|
| `prices` | `(trade_date, series_id)` | Precios diarios (cobre, DXY, oro, etc.) |
| `inventories` | `(trade_date, exchange, category)` | Stocks por bolsa |
| `cot` | `(report_date)` | Posicionamiento CFTC semanal |
| `macro` | `(obs_date, series_id)` | Indicadores macro |
| `spreads` | `(trade_date, spread_id)` | Spreads y ratios calculados |

Views útiles:

| View | Qué retorna |
|---|---|
| `clean.latest_prices` | Último precio por serie |
| `clean.latest_inventories` | Últimos inventarios por exchange |
| `clean.latest_cot` | Último reporte COT |
| `meta.series_coverage` | Cobertura temporal por serie |

## Fuentes y API keys

| Fetcher | Fuente | API Key | Nota |
|---|---|---|---|
| `fetch_comex.py` | Yahoo Finance (yfinance) | No requiere | |
| `fetch_cot.py` | CFTC (descarga CSV público) | No requiere | |
| `fetch_fred.py` | FRED API | `FRED_API_KEY` (gratis) | |
| `fetch_shfe.py` | SHFE endpoints JSON/HTML | No requiere | Lento desde fuera de China (~60s timeout) |

## Consultar datos

Desde Python:

```python
import sys; sys.path.insert(0, "datos/scripts")
from db import query

# Últimos precios
query("SELECT * FROM clean.latest_prices")

# Percentil COT
query("""
    SELECT report_date, managed_money_net,
           PERCENT_RANK() OVER (ORDER BY managed_money_net) AS pctl
    FROM clean.cot
    WHERE report_date >= current_date - INTERVAL '2 years'
    ORDER BY report_date DESC LIMIT 1
""")
```

Desde la CLI de DuckDB:

```bash
datos/.venv/bin/python -c "import duckdb; duckdb.connect('datos/cobre.duckdb').sql('SELECT * FROM clean.latest_prices').show()"
```
