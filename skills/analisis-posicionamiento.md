---
nombre: analisis-posicionamiento
descripcion: Analizar el reporte COT semanal y posicionamiento especulativo
nodos:
  - trading/posicionamiento
  - tecnico/senales
contexto_condicional:
  - si: extremo_historico
    agregar: [tecnico/indicadores, derivados/opciones-y-volatilidad]
inputs:
  - datos COT de la semana (managed money longs, shorts, net)
  - open interest total
outputs:
  - interpretación de posicionamiento
  - señal contrarian si aplica
  - relación con movimiento de precio
---

# Skill: Análisis de Posicionamiento

## Procedimiento

### 1. Datos de la semana
- Managed money: gross longs, gross shorts, net position
- Cambio semanal de cada uno
- Total open interest y cambio

### 2. Contexto histórico
- ¿Net position actual en qué percentil vs historia de 2 años?
- > 80th percentil: crowded long
- < 20th percentil: crowded short o muy under-owned
- ¿Cerca de máximo o mínimo histórico absoluto?

### 3. Ritmo de cambio
- ¿Cuánto cambió la net position esta semana?
- Cambio > 10k contratos = movimiento significativo
- ¿Es acumulación nueva o cierre de posiciones?
  - Si net longs suben y OI sube = nuevos longs (dinero nuevo)
  - Si net longs suben y OI baja = short covering (cierre de shorts)

### 4. Divergencias precio-posicionamiento
- Precio subiendo pero managed money reduciendo longs → divergencia bearish
- Precio cayendo pero managed money reduciendo shorts → divergencia bullish
- Precio estable pero posicionamiento moviéndose → anticipación de movimiento

### 5. Señal contrarian
- ¿Estamos en zona de extremo?
- Extremo long + señales técnicas de agotamiento → riesgo de corrección alto
- Extremo short + soporte técnico + fundamentales no tan malos → rebote probable
- Zona neutral → poca señal contrarian; seguir fundamentales

### 6. OI como señal de participación
- OI total creciendo → mercado atrayendo participación (confirma tendencia)
- OI total cayendo → participantes saliendo (tendencia puede agotarse)

### 7. Conclusión
- Sentimiento especulativo: bullish / bearish / neutral
- ¿Señal contrarian activa? Sí / No
- Convicción: alta / media / baja
