---
nombre: resumir-paper
descripcion: Resumir un paper o reporte y agregarlo al catálogo de referencias
nodos:
  - referencias/catalogo
  - referencias/por-tema
inputs:
  - paper o reporte (PDF, URL, o texto)
outputs:
  - resumen estructurado
  - entrada en el catálogo
  - actualización de referencias por tema
  - resumen detallado en referencias/resumenes/ si warranted
---

# Skill: Resumir Paper

## Procedimiento

### 1. Metadata
- Título
- Autores
- Año de publicación
- Fuente/journal
- Tema principal

### 2. Resumen ejecutivo
- ¿Cuál es la pregunta que aborda? (1 oración)
- ¿Cuál es la metodología principal? (1 oración)
- ¿Cuál es la conclusión principal? (1-2 oraciones)

### 3. Relevancia para el mercado del cobre
- ¿Qué aspecto del mercado ilumina?
- ¿Tiene implicaciones prácticas para análisis o trading?
- ¿Introduce un framework o modelo nuevo útil?
- Relevancia: alta / media / baja

### 4. Key findings (máximo 5)
- Los hallazgos más importantes, cada uno en 1-2 oraciones

### 5. Datos o modelos reutilizables
- ¿El paper provee datos que podemos incorporar?
- ¿Introduce un modelo que podemos referenciar en nuestros skills?
- ¿Tiene figuras o tablas clave?

### 6. Agregar al catálogo
- Crear entrada en `referencias/catalogo.md` con formato estándar
- Asignar código de referencia (P00X para papers, R00X para reportes)

### 7. Actualizar índice temático
- Agregar referencia en `referencias/por-tema.md` bajo los temas relevantes

### 8. Resumen detallado (si relevancia alta)
- Crear `referencias/resumenes/[codigo]-[titulo-breve].md`
- Incluir: contexto, metodología detallada, findings, implicaciones, datos clave
