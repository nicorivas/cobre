---
nombre: analisis-volatilidad
descripcion: Analizar condiciones de volatilidad y superficie de opciones
ruta: analisis-volatilidad
inputs:
  - datos de volatilidad implícita (ATM IV, skew, term structure)
  - volatilidad realizada reciente
outputs:
  - diagnóstico de régimen de volatilidad
  - oportunidades si las hay
  - implicaciones para hedging
---

# Skill: Análisis de Volatilidad

## Procedimiento

### 1. Nivel de IV ATM
- IV actual de opciones ATM (front month)
- Comparar con rango histórico (percentil de 1 año)
- < 15%: baja; 15-25%: normal; 25-35%: elevada; > 35%: muy alta

### 2. IV vs Realized Vol
- Calcular RV de los últimos 20 días (o usar dato disponible)
- Vol premium = IV - RV
- Premium > 5 puntos: opciones "caras" (favorece venta de vol)
- Premium < -3 puntos: opciones "baratas" (favorece compra de vol)

### 3. Skew
- Comparar IV de 25-delta puts vs 25-delta calls
- Skew positivo (puts más caras): mercado demanda protección downside
- Skew negativo (calls más caras): mercado teme upside/squeeze
- ¿Skew cambió significativamente vs semana anterior?

### 4. Term structure
- IV de front month vs 3M vs 6M
- Normal (upward): mercado espera más vol futura
- Invertida (downward): evento inminente, mercado espera calma después
- ¿Cambió la forma recientemente?

### 5. Catalizadores
- ¿Hay evento binario próximo? (FOMC, PMI, tariff decision, huelga)
- ¿La term structure refleja un evento específico?
- Post-evento: ¿la vol debería normalizarse?

### 6. Implicaciones para hedging
- IV alta → opciones caras → hedgers pueden preferir futuros o spreads
- IV baja → opciones baratas → buen momento para comprar protección
- Skew alto → collars más atractivos (vender call cara, comprar put cara)

### 7. Oportunidades de trading de vol
- ¿Vol crush post-evento probable? → vender straddles/strangles
- ¿Vol expansion pre-evento? → comprar vol antes del catalizador
- ¿Skew mispriced? → risk reversals
- ¿Term structure mispriced? → calendar spreads de vol
