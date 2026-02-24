---
nombre: procesar-noticia
descripcion: Procesar una noticia del mercado del cobre y actualizar el repo
nodos: []  # Depende del contenido de la noticia; se determina en paso 2
inputs:
  - texto de la noticia o URL
outputs:
  - clasificación de la noticia
  - actualización de temas-activos.md si aplica
  - entrada en noticias/log/ si relevante
---

# Skill: Procesar Noticia

## Procedimiento

### 1. Leer y resumir
- ¿De qué trata la noticia? (1-2 oraciones)
- ¿Fuente confiable?
- ¿Es información nueva o reciclada?

### 2. Clasificar
- Categoría principal: oferta / demanda / macro / geopolítica / derivados / ESG / otra
- Subcategoría: disrupción / política / dato / M&A / regulación / etc.
- Relevancia para precio: alta / media / baja

### 3. Identificar nodos afectados
- Consultar `indice.yaml` por tags relevantes
- Listar nodos que deberían actualizarse con esta información

### 4. Evaluar impacto
- ¿Bullish o bearish para el precio del cobre?
- ¿Magnitud? (mueve mercado, informativo, noise)
- ¿Timing? (inmediato, semanas, meses)
- ¿El mercado ya incorporó esta información?

### 5. ¿Es tema nuevo o update de tema existente?
- Revisar `noticias/temas-activos.md`
- Si es tema nuevo → agregar con formato estándar
- Si es update → actualizar el tema existente
- Si el tema se resolvió → marcar como resuelto

### 6. Logging (opcional)
- Para noticias de alta relevancia, crear entrada en `noticias/log/`
- Formato: `YYYY-MM-DD-titulo-breve.md`
- Contenido: resumen, clasificación, impacto, fuente

### 7. Actualizar nodos si necesario
- Si la noticia contiene información factual nueva (e.g., nueva producción, cierre de mina)
- Actualizar el nodo correspondiente con la nueva información
- Marcar con fecha de actualización
