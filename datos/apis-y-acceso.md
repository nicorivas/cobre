---
nodo: datos/apis-y-acceso
---

# APIs y Acceso a Datos

## APIs gratuitas

### FRED (Federal Reserve Economic Data)
- URL: https://fred.stlouisfed.org/
- Datos: DXY, tasas de interés, PMI, industrial production
- API: REST, requiere API key (gratis)
- No tiene precios de cobre directamente pero sí macro indicators

### World Bank Open Data
- URL: https://data.worldbank.org/
- Datos: PIB, población, commodity prices históricos (mensual)
- API: REST, gratis, sin key
- Commodity prices incluyen cobre (promedios mensuales)

### CFTC COT Data
- URL: https://www.cftc.gov/MarketReports/CommitmentsofTraders/
- Datos: posicionamiento por categoría de participante
- Formato: CSV descargable, actualizado semanalmente
- No hay API formal pero se puede scrape automatizado

### LME Datos Básicos
- URL: https://www.lme.com/
- Datos: precios de cierre, inventarios, volúmenes (básico)
- API: LME DataStore para datos detallados (suscripción)

### CME Datos Básicos
- URL: https://www.cmegroup.com/
- Datos: settlements, volumen, OI, stocks
- API: CME DataMine (suscripción), pero datos básicos en web gratis

## APIs de pago

### LME DataStore
- Datos: precios tick-by-tick, forward curves, inventarios por warehouse, turnover
- Formato: REST API, FTP
- Costo: varía por dataset (~$5,000-50,000/año)

### CME DataMine
- Datos: market data histórico, settlements, Greeks, OI detallado
- Formato: CSV, API
- Costo: varía por dataset

### Bloomberg Terminal (BLPAPI)
- API: Bloomberg API (Python, Java, C++)
- Datos: todo (precios, fundamentales, analytics, noticias)
- Costo: ~$24,000/año por terminal

### Refinitiv (LSEG)
- API: Refinitiv Data Platform, Eikon Data API
- Datos: similar a Bloomberg
- Costo: variable

### Nasdaq Data Link (ex-Quandl)
- URL: https://data.nasdaq.com/
- Datos: commodity futures, macro, algunos LME
- API: REST, Python library
- Costo: gratis (datasets limitados) o suscripción

## Acceso alternativo

### Yahoo Finance (yfinance)
- Datos: precios COMEX HG futures (delayed), ETFs de cobre
- API: no oficial, library Python `yfinance`
- Limitaciones: no LME, no inventarios, no COT

### Investing.com
- Datos: precios de mercado amplios incluyendo cobre
- API: no oficial, web scraping posible
- Useful para datos quick-and-dirty

### Westmetall
- URL: https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Cu_cash
- Datos: LME Copper Cash Settlement, 3-Month, y stocks totales (diarios)
- Acceso: gratis, sin API key, datos desde 2008
- Formato: HTML tabular, parseable con BeautifulSoup
- Delay: 1 día hábil

## Consideraciones

- **Datos de bolsa en tiempo real**: siempre de pago
- **Datos delayed (15-30 min)**: a veces gratis
- **Datos de fin de día**: más fáciles de obtener gratis
- **Fundamentales (inventarios, posicionamiento)**: mayormente gratis para los básicos
- **Premiums y TC/RC**: siempre de pago (Fastmarkets, CRU)
- **Cost curves**: siempre de pago (Wood Mac, CRU)

## Pipeline automatizado

Las fuentes marcadas arriba como gratuitas están integradas en el pipeline
de datos del repo (`datos/scripts/`). Ver `datos/README.md` para setup y uso.

| Script | Fuente | Datos | API key |
|---|---|---|---|
| `fetch_comex.py` | Yahoo Finance | COMEX HG, DXY, Gold, US 10Y, S&P 500 | No |
| `fetch_lme.py` | Westmetall | LME Cash, 3M, stocks | No |
| `fetch_cot.py` | CFTC | COT managed money, producers, swap dealers | No |
| `fetch_fred.py` | FRED | Fed Funds, Industrial Production, Trade Weighted USD | Sí (gratis) |
| `calc_spreads.py` | Calculado | COMEX-LME arb, LME Cash-3M, Cu/Au ratio | N/A |
