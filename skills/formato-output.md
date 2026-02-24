# Formato Estándar de Output

Todos los análisis producidos por skills deben seguir este formato.
El objetivo es que los outputs sean **escaneables, comparables y auditables** —
el usuario siempre debe poder evaluar la lógica detrás de cada conclusión.

## Estructura base

```markdown
---
fecha: YYYY-MM-DD
skill: nombre-del-skill
input: descripción breve del input
nodos: [nodos consultados del indice.yaml]
---

## TL;DR
> 1-2 oraciones con la conclusión principal. Solo el "qué", no el "por qué".

## Veredicto
[Tabla estandarizada por categoría — ver variantes abajo]

## Análisis
[Cuerpo libre, específico al skill. Datos, interpretación, tablas, comparaciones.]

## Implicaciones
- Qué significa esto para el mercado, posiciones, o decisiones concretas.

## Vigilar
- [ ] Triggers, indicadores o eventos a monitorear como consecuencia.
- [ ] Con horizonte temporal si es posible.

## Cambios al repo
- [ ] Nodos a actualizar con información nueva.
- [ ] Temas activos a agregar o modificar.
- (o "Ninguno" si no aplica.)
```

## Variantes de veredicto

Hay tres variantes según el tipo de skill. Todas incluyen una **justificación
verbal** que explica el razonamiento detrás de la clasificación. El usuario
debe poder leer la justificación y decidir si está de acuerdo o no con la
lógica — el veredicto nunca debe ser una caja negra.

### Señal de mercado

Para: `interpretar-inventarios`, `analisis-posicionamiento`, `analisis-volatilidad`,
`analisis-tecnico`, `analisis-spreads`, `analisis-curva-forward`, `analisis-tcrc`.

```markdown
| Campo | Valor |
|---|---|
| Señal | bullish / bearish / neutral / mixto |
| Magnitud | alta / media / baja |
| Confianza | alta / media / baja |
| Justificación | [1-3 oraciones explicando el razonamiento: qué datos o condiciones llevan a esta señal, y por qué esa magnitud y confianza. Si hay factores que podrían invalidar la conclusión, mencionarlos.] |
```

Ejemplo:

```markdown
| Campo | Valor |
|---|---|
| Señal | bearish |
| Magnitud | media |
| Confianza | alta |
| Justificación | LME on-warrant subió 45 kt en una semana, el mayor build desde marzo. El movimiento coincide con arrivals de metal redireccionado desde COMEX, no con surplus de producción. Si se confirma que es un one-off por reposicionamiento post-tariff, la señal se debilita. |
```

### Evento

Para: `procesar-noticia`, `monitor-china`, y análisis ad hoc de eventos.

```markdown
| Campo | Valor |
|---|---|
| Impacto | bullish / bearish / neutral / mixto |
| Magnitud | alta / media / baja |
| Horizonte | inmediato / semanas / meses |
| Priced-in | sí / parcialmente / no |
| Justificación | [1-3 oraciones: por qué este evento tiene este impacto direccional, por qué esa magnitud, y cómo se evaluó si el mercado ya lo incorporó. Mencionar qué cambiaría la conclusión.] |
```

Ejemplo:

```markdown
| Campo | Valor |
|---|---|
| Impacto | mixto |
| Magnitud | media |
| Horizonte | semanas |
| Priced-in | parcialmente |
| Justificación | El tariff de 10% reemplaza un régimen de 10-50% por país, lo que reduce la distorsión neta pero no la elimina. Es bearish para COMEX premium (tariff efectivo menor) pero alivia tightness artificial fuera de EE.UU. El mercado anticipaba el fallo judicial pero no el reemplazo inmediato bajo Section 122. Si Trump ejecuta la subida a 15%, la conclusión gira a bearish para LME por renovado drenaje de metal. |
```

### Evaluación

Para: `evaluar-proyecto-minero`, `evaluar-impacto-esg`, `analisis-cost-curve`.

```markdown
| Campo | Valor |
|---|---|
| Resultado | viable / riesgoso / inviable — o — alto / medio / bajo |
| Riesgo principal | [identificar el riesgo dominante] |
| Horizonte | corto / medio / largo plazo |
| Confianza | alta / media / baja |
| Justificación | [1-3 oraciones: qué evidencia soporta el resultado, por qué ese riesgo es el principal, y qué supuestos críticos se están haciendo. Mencionar qué haría cambiar la evaluación.] |
```

Ejemplo:

```markdown
| Campo | Valor |
|---|---|
| Resultado | riesgoso |
| Riesgo principal | permitting — sin EIS aprobado y con oposición activa de comunidades |
| Horizonte | largo plazo (primera producción 2031+) |
| Confianza | media |
| Justificación | El proyecto tiene ley atractiva (0.9% Cu) y estaría en Q2 de la cost curve, pero no tiene permisos ambientales clave. El operador tiene track record mixto en jurisdicciones similares. Si se resuelve el EIS en 2027, la evaluación sube a viable — pero proyectos comparables en esta jurisdicción han tardado 5+ años en permitting. |
```

## Análisis semanal

El skill `analisis-semanal` es un caso especial: cubre múltiples dimensiones.
Usa la tabla de **señal de mercado** para la síntesis final, y dentro de la
sección de Análisis puede usar mini-veredictos por dimensión:

```markdown
## Análisis

### Inventarios
[Datos y análisis]
> Señal: bearish (media) — LME on-warrant cayó 20 kt, days of coverage en 3.2 días.

### Posicionamiento
[Datos y análisis]
> Señal: neutral — managed money en percentil 55, sin extremo ni divergencia.

### Estructura de término
[Datos y análisis]
> Señal: bullish (baja) — cash-3M back se amplió $5 pero desde nivel bajo.

[... etc.]
```

Los mini-veredictos no necesitan tabla completa — basta una línea con señal,
magnitud y justificación breve. El veredicto principal del análisis sintetiza
todas las dimensiones.

## Notas

- **No inventar datos**: si un dato no está disponible, decirlo explícitamente.
  Nunca rellenar con estimaciones no declaradas como tales.
- **Declarar supuestos**: si la conclusión depende de un supuesto (e.g., "asumiendo
  que China no retalia"), hacerlo explícito en la justificación.
- **Contraargumentos**: la justificación debe mencionar al menos un factor que
  podría invalidar la conclusión. Si no hay ninguno, la confianza probablemente
  debería ser "alta".
- **Fecha**: siempre incluir la fecha. Los análisis de mercado pierden valor rápido.
