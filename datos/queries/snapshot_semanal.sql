-- snapshot_semanal.sql
-- Query para el skill analisis-semanal: estado completo del mercado.
-- Retorna los datos más recientes de cada dimensión.

-- 1. Precios actuales y cambio semanal
WITH latest AS (
    SELECT series_id, trade_date, close
    FROM clean.prices
    WHERE trade_date = (SELECT max(trade_date) FROM clean.prices)
),
week_ago AS (
    SELECT series_id, close
    FROM clean.prices
    WHERE trade_date = (
        SELECT max(trade_date) FROM clean.prices
        WHERE trade_date <= (SELECT max(trade_date) - INTERVAL '7 days' FROM clean.prices)
    )
)
SELECT
    l.series_id,
    l.trade_date AS fecha,
    l.close AS precio_actual,
    w.close AS precio_semana_ant,
    round((l.close - w.close) / w.close * 100, 2) AS cambio_pct
FROM latest l
LEFT JOIN week_ago w USING (series_id)
ORDER BY l.series_id;

-- 2. Último COT con percentil histórico (2 años)
SELECT
    c.report_date,
    c.managed_money_net,
    c.managed_money_long,
    c.managed_money_short,
    c.total_oi,
    round(PERCENT_RANK() OVER (ORDER BY c.managed_money_net) * 100, 1) AS percentil_2y
FROM clean.cot c
WHERE c.report_date >= (SELECT max(report_date) - INTERVAL '2 years' FROM clean.cot)
ORDER BY c.report_date DESC
LIMIT 5;

-- 3. Spreads calculados (últimos 5 días)
SELECT trade_date, spread_id, round(value, 4) AS valor
FROM clean.spreads
WHERE trade_date >= (SELECT max(trade_date) - INTERVAL '7 days' FROM clean.spreads)
ORDER BY spread_id, trade_date DESC;
