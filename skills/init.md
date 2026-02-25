---
nombre: init
descripcion: Inicialización del asistente — orientarse en el repo y reportar estado
inputs:
  - ninguno (se corre al inicio de una sesión)
outputs:
  - resumen del estado actual del mercado y los datos
  - skills disponibles
  - sugerencia de siguiente paso
---

# Skill: Inicialización

Correr al inicio de cada sesión para orientar al asistente y al usuario.

## Procedimiento

### 1. Cargar contexto base
- Leer `indice.yaml` (siempre primero)
- Leer `noticias/temas-activos.md` para contexto de mercado actual

### 2. Verificar estado de datos
- Conectar a `datos/cobre.duckdb`
- Ejecutar:

```sql
SELECT series_id, max(trade_date) AS ultimo_dato,
       current_date - max(trade_date) AS dias_atraso
FROM clean.prices
GROUP BY series_id
ORDER BY dias_atraso DESC;
```

- Si alguna serie tiene >3 días de atraso en día hábil, sugerir correr
  `datos/.venv/bin/python datos/scripts/fetch_all.py`
- Si la DB no existe, indicar que hay que correr el setup inicial
  (ver datos/README.md)

### 3. Reportar estado

Formato del reporte:

```
## Estado del asistente

**Datos**: [actualizados / desactualizados N días / sin inicializar]
**Último precio**: COMEX $X.XX/lb | LME $X/t | SHFE ¥X/t
**Temas activos**: [lista breve de temas de noticias/temas-activos.md]

## Skills disponibles

| Skill | Qué hace |
|---|---|
| analisis-semanal | Revisión semanal completa del mercado |
| analisis-posicionamiento | Analizar COT semanal y señales contrarian |
| analisis-tecnico | Evaluar niveles técnicos y señales |
| analisis-spreads | Analizar spreads inter/intra-market |
| analisis-curva-forward | Interpretar estructura de término |
| analisis-volatilidad | Evaluar superficie de vol y régimen |
| analisis-cost-curve | Precio actual vs curva de costos |
| analisis-tcrc | Analizar mercado de TC/RC |
| interpretar-inventarios | Interpretar movimientos de stocks |
| monitor-china | Evaluar impacto de noticias/datos chinos |
| evaluar-proyecto-minero | Evaluar viabilidad de proyecto minero |
| evaluar-impacto-esg | Evaluar impacto ESG en mercado |
| procesar-noticia | Procesar noticia y actualizar repo |
| resumir-paper | Resumir paper/reporte y catalogar |
| actualizar-temas-activos | Revisar y actualizar temas del mercado |

Para ejecutar un skill, pide el análisis correspondiente.
Por ejemplo: "hazme el análisis semanal" o "procesa esta noticia: [texto]".

## ¿Qué quieres hacer?

[Sugerir acción basada en contexto: si datos están viejos, actualizar.
Si hay temas activos relevantes, ofrecer profundizar. Si es lunes,
sugerir análisis semanal.]
```

### 4. Sugerir siguiente paso

Basado en:
- **Día de la semana**: lunes → sugerir análisis semanal
- **Datos desactualizados**: sugerir fetch_all.py
- **Temas activos urgentes**: ofrecer profundizar en el más relevante
- **Sin temas activos**: sugerir buscar noticias recientes
- **Primera sesión** (temas-activos vacío, DB vacía): guiar setup completo
