---
nombre: actualizar-temas-activos
descripcion: Revisar y actualizar el snapshot de temas activos del mercado
nodos:
  - noticias/temas-activos
  - noticias/fuentes
inputs:
  - noticias recientes procesadas
  - estado actual de temas-activos.md
outputs:
  - temas-activos.md actualizado
  - temas nuevos agregados, resueltos archivados
---

# Skill: Actualizar Temas Activos

## Procedimiento

### 1. Revisar estado actual
- Leer `noticias/temas-activos.md`
- Para cada tema activo: ¿sigue vigente? ¿Hay update?

### 2. Evaluar temas existentes
Para cada tema:
- ¿Ha habido desarrollos nuevos? → actualizar descripción y fecha
- ¿El impacto cambió? (bullish/bearish/magnitud) → actualizar
- ¿Se resolvió? → marcar como "resuelto" con nota de resolución
- ¿Perdió relevancia sin resolverse? → bajar magnitud o archivar

### 3. Identificar temas nuevos
- Revisar noticias procesadas desde última actualización
- ¿Hay temas nuevos que no están en la lista?
- Solo agregar si el tema tiene impacto medio o alto y es likely to persist

### 4. Priorizar
- Ordenar temas por magnitud de impacto (alta → baja)
- Los temas de alta magnitud van primero
- Máximo ~5-8 temas activos simultáneamente (evitar lista interminable)

### 5. Escribir actualizaciones
- Para cada tema nuevo: usar formato estándar de `noticias/temas-activos.md`
- Para updates: agregar línea de "Última actualización" con fecha y cambio
- Para resueltos: mover a sección "Resueltos" con fecha y resolución

### 6. Consistencia
- ¿Los temas activos son coherentes con la posición general del mercado?
- ¿Falta algún tema obvio?
- ¿Algún tema contradice otro? (puede ser válido pero hay que notarlo)
