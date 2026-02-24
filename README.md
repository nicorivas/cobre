# Cobre — Base de Conocimiento del Mercado del Cobre

Repositorio de conocimiento estructurado para el análisis del mercado del cobre,
diseñado para ser navegado tanto por humanos como por agentes AI.

## Qué es esto

Una base de conocimiento que cubre:
- **Fundamentos**: oferta, demanda, balance, costos, scrap, TC/RC
- **Pricing**: mecanismos de precio, curva forward, premiums, ratios cross-asset
- **Trading**: inventarios, flujos comerciales, posicionamiento especulativo
- **Derivados**: futuros, opciones, volatilidad, spreads, coberturas
- **Análisis técnico**: indicadores, estructura de mercado, señales
- **Macro**: ciclos, China, transición energética, geopolítica
- **ESG**: frameworks, regulación, carbono
- **Skills**: procedimientos analíticos reutilizables

## Cómo navegar

El archivo `indice.yaml` es el **grafo de conocimiento** central. Define cada documento
como un nodo con:
- `resumen`: qué contiene
- `tags`: temas que cubre
- `requiere`: documentos que hay que leer antes
- `alimenta`: documentos que usan este como input
- `relacionado`: documentos con temas que se solapan

Las **rutas** en el índice son secuencias predefinidas de nodos para análisis comunes
(evaluar una disrupción, analizar demanda china, diseñar cobertura, etc.).

## Para agentes AI

Ver `CLAUDE.md` para instrucciones detalladas de navegación.
