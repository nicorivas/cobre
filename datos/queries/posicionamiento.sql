-- posicionamiento.sql
-- Query para el skill analisis-posicionamiento.

-- 1. Últimos 10 reportes COT con cambio semanal
WITH ordered AS (
    SELECT
        report_date,
        managed_money_long,
        managed_money_short,
        managed_money_net,
        total_oi,
        managed_money_net - LAG(managed_money_net) OVER (ORDER BY report_date) AS net_change,
        total_oi - LAG(total_oi) OVER (ORDER BY report_date) AS oi_change
    FROM clean.cot
    ORDER BY report_date DESC
)
SELECT * FROM ordered LIMIT 10;

-- 2. Percentil histórico (últimos 2 años)
SELECT
    report_date,
    managed_money_net,
    round(PERCENT_RANK() OVER (ORDER BY managed_money_net) * 100, 1) AS percentil
FROM clean.cot
WHERE report_date >= (SELECT max(report_date) - INTERVAL '2 years' FROM clean.cot)
ORDER BY report_date DESC
LIMIT 1;

-- 3. Extremos históricos (para contexto)
SELECT
    'max' AS tipo,
    report_date,
    managed_money_net
FROM clean.cot
WHERE managed_money_net = (SELECT max(managed_money_net) FROM clean.cot)
UNION ALL
SELECT
    'min' AS tipo,
    report_date,
    managed_money_net
FROM clean.cot
WHERE managed_money_net = (SELECT min(managed_money_net) FROM clean.cot);

-- 4. Divergencia precio-posicionamiento (últimas 4 semanas)
WITH weekly_cot AS (
    SELECT report_date, managed_money_net
    FROM clean.cot
    ORDER BY report_date DESC
    LIMIT 4
),
weekly_price AS (
    SELECT trade_date, close
    FROM clean.prices
    WHERE series_id = 'comex_hg'
    ORDER BY trade_date DESC
    LIMIT 20
)
SELECT
    c.report_date,
    c.managed_money_net,
    p.close AS comex_price,
    c.managed_money_net - LAG(c.managed_money_net) OVER (ORDER BY c.report_date) AS net_change
FROM weekly_cot c
LEFT JOIN LATERAL (
    SELECT close FROM weekly_price p
    WHERE p.trade_date <= c.report_date
    ORDER BY p.trade_date DESC
    LIMIT 1
) p ON true
ORDER BY c.report_date DESC;
