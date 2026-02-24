-- schema.sql — DDL para la base de datos de mercado del cobre
-- Ejecutar con: python datos/scripts/init_db.py
-- ================================================================

-- ══════════════════════════════════════════════════════════════════
-- SCHEMAS
-- ══════════════════════════════════════════════════════════════════

CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS clean;
CREATE SCHEMA IF NOT EXISTS meta;

-- ══════════════════════════════════════════════════════════════════
-- META: catálogo de series y metadata
-- ══════════════════════════════════════════════════════════════════

CREATE TABLE IF NOT EXISTS meta.series_catalog (
    series_id     TEXT PRIMARY KEY,
    name          TEXT NOT NULL,
    source        TEXT NOT NULL,        -- 'yfinance', 'fred', 'cftc', 'lme', 'cme', 'calculated'
    frequency     TEXT NOT NULL,        -- 'daily', 'weekly', 'monthly'
    unit          TEXT NOT NULL,        -- 'usd_per_ton', 'usd_per_lb', 'index', 'contracts', 'metric_tons', 'pct'
    description   TEXT
);

-- ══════════════════════════════════════════════════════════════════
-- RAW: datos inmutables tal como llegaron
-- ══════════════════════════════════════════════════════════════════

CREATE SEQUENCE IF NOT EXISTS raw.ingestion_seq START 1;

CREATE TABLE IF NOT EXISTS raw.ingestions (
    ingestion_id  INTEGER DEFAULT nextval('raw.ingestion_seq') PRIMARY KEY,
    source        TEXT NOT NULL,
    fetched_at    TIMESTAMP NOT NULL DEFAULT now(),
    status        TEXT NOT NULL DEFAULT 'ok',   -- 'ok', 'partial', 'error'
    row_count     INTEGER,
    notes         TEXT
);

CREATE TABLE IF NOT EXISTS raw.series_data (
    ingestion_id  INTEGER NOT NULL REFERENCES raw.ingestions(ingestion_id),
    series_id     TEXT NOT NULL,
    trade_date    DATE NOT NULL,
    value         DOUBLE,
    high          DOUBLE,
    low           DOUBLE,
    volume        DOUBLE,
    unit          TEXT
);

-- ══════════════════════════════════════════════════════════════════
-- CLEAN: normalizado, deduplicado, consultable
-- ══════════════════════════════════════════════════════════════════

-- Precios diarios (cobre, DXY, oro, etc.)
CREATE TABLE IF NOT EXISTS clean.prices (
    trade_date    DATE NOT NULL,
    series_id     TEXT NOT NULL,
    close         DOUBLE NOT NULL,
    high          DOUBLE,
    low           DOUBLE,
    volume        DOUBLE,
    unit          TEXT NOT NULL DEFAULT 'usd_per_ton',
    updated_at    TIMESTAMP NOT NULL DEFAULT now(),
    PRIMARY KEY (trade_date, series_id)
);

-- Inventarios por exchange y categoría
CREATE TABLE IF NOT EXISTS clean.inventories (
    trade_date    DATE NOT NULL,
    exchange      TEXT NOT NULL,        -- 'lme', 'comex', 'shfe'
    category      TEXT NOT NULL,        -- 'total', 'on_warrant', 'cancelled', 'registered', 'eligible'
    volume_mt     DOUBLE NOT NULL,      -- siempre en toneladas métricas
    updated_at    TIMESTAMP NOT NULL DEFAULT now(),
    PRIMARY KEY (trade_date, exchange, category)
);

-- Posicionamiento CFTC COT
CREATE TABLE IF NOT EXISTS clean.cot (
    report_date           DATE PRIMARY KEY,  -- martes al que refiere el reporte
    managed_money_long    INTEGER,
    managed_money_short   INTEGER,
    managed_money_net     INTEGER,
    producer_long         INTEGER,
    producer_short        INTEGER,
    producer_net          INTEGER,
    swap_dealer_long      INTEGER,
    swap_dealer_short     INTEGER,
    swap_dealer_net       INTEGER,
    total_oi              INTEGER,
    updated_at            TIMESTAMP NOT NULL DEFAULT now()
);

-- Indicadores macro (formato largo)
CREATE TABLE IF NOT EXISTS clean.macro (
    obs_date      DATE NOT NULL,
    series_id     TEXT NOT NULL,
    value         DOUBLE NOT NULL,
    updated_at    TIMESTAMP NOT NULL DEFAULT now(),
    PRIMARY KEY (obs_date, series_id)
);

-- Spreads y ratios calculados
CREATE TABLE IF NOT EXISTS clean.spreads (
    trade_date    DATE NOT NULL,
    spread_id     TEXT NOT NULL,        -- 'lme_cash_3m', 'comex_lme_arb', 'cu_au_ratio'
    value         DOUBLE NOT NULL,
    unit          TEXT,
    updated_at    TIMESTAMP NOT NULL DEFAULT now(),
    PRIMARY KEY (trade_date, spread_id)
);

-- ══════════════════════════════════════════════════════════════════
-- VIEWS: consultas preconstruidas
-- ══════════════════════════════════════════════════════════════════

-- Último dato disponible por serie de precios
CREATE OR REPLACE VIEW clean.latest_prices AS
SELECT p.series_id, p.trade_date, p.close, p.high, p.low, p.unit
FROM clean.prices p
INNER JOIN (
    SELECT series_id, max(trade_date) AS max_date
    FROM clean.prices
    GROUP BY series_id
) latest ON p.series_id = latest.series_id AND p.trade_date = latest.max_date;

-- Últimos inventarios por exchange
CREATE OR REPLACE VIEW clean.latest_inventories AS
SELECT i.exchange, i.category, i.trade_date, i.volume_mt
FROM clean.inventories i
INNER JOIN (
    SELECT exchange, category, max(trade_date) AS max_date
    FROM clean.inventories
    GROUP BY exchange, category
) latest ON i.exchange = latest.exchange
    AND i.category = latest.category
    AND i.trade_date = latest.max_date;

-- Último reporte COT
CREATE OR REPLACE VIEW clean.latest_cot AS
SELECT * FROM clean.cot
WHERE report_date = (SELECT max(report_date) FROM clean.cot);

-- Cobertura temporal por serie
CREATE OR REPLACE VIEW meta.series_coverage AS
SELECT
    s.series_id,
    s.name,
    s.source,
    s.frequency,
    s.unit,
    min(p.trade_date) AS first_date,
    max(p.trade_date) AS last_date,
    count(p.trade_date) AS data_points
FROM meta.series_catalog s
LEFT JOIN clean.prices p ON s.series_id = p.series_id
GROUP BY s.series_id, s.name, s.source, s.frequency, s.unit;
