# CLAUDE.md — Instrucciones para agentes AI

Este repositorio es una base de conocimiento estructurada sobre el mercado del cobre.
Está diseñado para ser navegado por agentes AI que asisten en análisis de mercado.

## Navegación del conocimiento

Este repo está organizado como un **grafo**. SIEMPRE lee `indice.yaml` antes
de cualquier análisis. El índice contiene:

- **nodos**: cada documento con resumen, tags, y conexiones direccionales
- **rutas**: secuencias predefinidas para análisis comunes

### Para encontrar información relevante:

1. Lee `indice.yaml`
2. Si la pregunta matchea una **ruta** predefinida → sigue esa secuencia de nodos
3. Si no → busca por **tags** en los nodos
4. Expande con `requiere` (contexto previo necesario) y `alimenta` (implicaciones downstream)
5. Carga **solo** los archivos identificados, no todo el repo

### Relaciones entre nodos:

| Campo | Significado | Dirección |
|---|---|---|
| `requiere` | Para entender este doc, primero lee estos | upstream → este nodo |
| `alimenta` | Este doc es input para estos otros | este nodo → downstream |
| `relacionado` | Temas que se solapan (bidireccional) | este nodo ↔ otro nodo |

## Estructura del repo

```
cobre/
├── indice.yaml          ← LEER PRIMERO: grafo de conocimiento
├── fundamentos/         ← Oferta, demanda, balance, costos, scrap, TC/RC
├── pricing/             ← Mecanismos de precio, curva forward, premiums, cross-asset
├── trading/             ← Inventarios, flujos, posicionamiento, estacionalidad
├── derivados/           ← Futuros, opciones, volatilidad, spreads, coberturas
├── tecnico/             ← Indicadores técnicos, estructura, señales
├── macro/               ← Ciclos, China, transición energética, geopolítica
├── esg/                 ← Frameworks, regulatorio, carbono, impacto en mercado
├── datos/               ← Fuentes, APIs, series clave
├── referencias/         ← Catálogo de papers, reportes, resúmenes
├── noticias/            ← Fuentes, temas activos, log de noticias procesadas
├── skills/              ← Procedimientos analíticos reutilizables
└── glosario.md          ← Definiciones de términos del mercado
```

## Skills

Los skills en `skills/` son procedimientos analíticos paso a paso. Cada skill:
- Declara una **ruta** del `indice.yaml` o lista nodos específicos como contexto
- Define **inputs** (qué necesita del usuario) y **outputs** (qué produce)
- Tiene un **procedimiento** numerado a seguir

Para ejecutar un skill: lee el skill → carga el contexto declarado → sigue el procedimiento.

**Formato de output**: todo análisis debe seguir el formato estándar definido en
`skills/formato-output.md`. Incluir siempre el veredicto con justificación verbal
que permita al usuario auditar la lógica.

## Convenciones

- Los archivos de contenido usan Markdown con encabezados jerárquicos
- Cada archivo empieza con un bloque de metadata en YAML front matter
- Las fechas usan formato ISO 8601 (YYYY-MM-DD)
- Los precios se expresan en USD/t (tonelada métrica) salvo indicación contraria
- Las cantidades se expresan en kt (miles de toneladas) o Mt (millones de toneladas)
- COMEX usa lbs; convertir a USD/t cuando se compara con LME (1 t = 2,204.62 lbs)
- Los tags en `indice.yaml` usan minúsculas, sin acentos, con guiones

## Mantenimiento del repo

Al agregar un nuevo documento:
1. Crear el archivo .md con front matter
2. Agregar el nodo correspondiente a `indice.yaml` con tags, resumen y conexiones
3. Actualizar las conexiones de nodos existentes que se relacionen

Al procesar una noticia:
1. Usar el skill `skills/procesar-noticia.md`
2. El skill actualiza `noticias/temas-activos.md` y opcionalmente el log
