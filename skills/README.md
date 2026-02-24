# Skills — Procedimientos Analíticos Reutilizables

Los skills son procedimientos paso a paso que un agente puede ejecutar para
realizar análisis específicos del mercado del cobre.

## Estructura de un skill

Cada skill tiene:

```yaml
---
nombre: nombre-del-skill
descripcion: Qué hace este skill
ruta: nombre-de-ruta-en-indice    # Si usa una ruta predefinida
nodos: [lista/de/nodos]           # O lista explícita de nodos necesarios
contexto_condicional:             # Contexto adicional según la situación
  - si: condicion
    agregar: [nodos/adicionales]
inputs:                           # Qué necesita del usuario
  - nombre: descripcion
outputs:                          # Qué produce
  - tipo: descripcion
---
```

Seguido de un **procedimiento** numerado que el agente ejecuta paso a paso.

## Tipos de skills

### Skills de análisis
Procedimientos para analizar aspectos específicos del mercado.

| Skill | Cuándo usar |
|---|---|
| `analisis-semanal` | Cada inicio de semana para revisión del mercado |
| `interpretar-inventarios` | Cuando hay movimiento relevante en stocks |
| `analisis-tcrc` | Cuando cambian TC/RC o hay noticia de smelters |
| `analisis-curva-forward` | Cuando la estructura de término cambia |
| `analisis-cost-curve` | Para evaluar sostenibilidad de niveles de precio |
| `analisis-posicionamiento` | Cuando sale el COT report semanal |
| `analisis-tecnico` | Para evaluar niveles y señales técnicas |
| `analisis-volatilidad` | Cuando la vol implícita cambia significativamente |
| `analisis-spreads` | Cuando hay movimientos relevantes en spreads |
| `monitor-china` | Cuando sale dato macro chino o noticia de política |
| `evaluar-proyecto-minero` | Para evaluar un proyecto de desarrollo |
| `evaluar-impacto-esg` | Para evaluar impacto ESG en un activo o mercado |

### Meta-skills (mantenimiento del repo)
Procedimientos para mantener el repo actualizado.

| Skill | Cuándo usar |
|---|---|
| `procesar-noticia` | Cuando se recibe una noticia relevante |
| `resumir-paper` | Cuando se agrega un nuevo paper/reporte al catálogo |
| `actualizar-temas-activos` | Periódicamente para mantener el snapshot actualizado |
