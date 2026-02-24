---
nombre: monitor-china
descripcion: Evaluar impacto de noticias o datos chinos en el mercado del cobre
ruta: cambio-demanda-china
inputs:
  - noticia o dato macro chino
outputs:
  - evaluación de impacto en demanda y precio de cobre
  - sectores afectados
  - indicadores a seguir
---

# Skill: Monitor China

## Procedimiento

### 1. Clasificar el evento
- ¿Dato macro? (PMI, imports, property, credit)
- ¿Política de estímulo? (recorte de tasas, fiscal, sectorial)
- ¿Regulación? (restricción, liberalización)
- ¿Sector específico? (property, grid, EVs, AC)

### 2. Cargar contexto
- Leer `macro/china` para contexto de sectores y políticas
- ¿Este evento es nuevo o continuación de tendencia conocida?

### 3. Evaluar impacto directo en demanda de Cu
- ¿Qué sector(es) de demanda de cobre afecta?
- ¿El impacto es positivo o negativo para demanda?
- ¿Magnitud? (marginal, moderado, significativo)
- ¿Timing? (inmediato, 3-6 meses, largo plazo)

### 4. Check de indicadores
- Yangshan premium: ¿moviéndose en la dirección coherente?
- SHFE stocks: ¿cambiando?
- LME-SHFE import arb: ¿ventana se abrió/cerró?
- China copper imports (si dato disponible)

### 5. Evaluar impacto secundario
- ¿Afecta fundiciones chinas? (TC/RC, producción de refinado)
- ¿Afecta importaciones de concentrado?
- ¿Afecta flujos de scrap?

### 6. Sentimiento de mercado
- ¿El mercado ya priced-in este evento?
- ¿La reacción de precio fue proporcional al impacto esperado?
- ¿Oportunidad si el mercado sobrerreaccionó o subreaccionó?

### 7. Conclusión
- Impacto en demanda china de Cu: positivo / negativo / neutral
- Magnitud: alta / media / baja
- Horizonte temporal: corto / medio / largo plazo
- Actualizar `noticias/temas-activos.md` si es tema nuevo o cambio material
