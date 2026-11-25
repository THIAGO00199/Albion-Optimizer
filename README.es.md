# Albion Optimizer — Calculadora de fabricación y beneficio de pociones

Optimizador de línea de comandos para recetas de pociones de Albion Online. Compara opciones de fabricación usando precios y supuestos introducidos por el jugador.

## Funciones

- Recetas de pociones de los niveles T2–T8.
- Cálculo de cantidades de fabricación y materiales.
- Modelado de la tasa de retorno de recursos (RRR) a partir del bono de producción indicado.
- Costos de estación, impuestos de venta, tarifas, materiales, ingresos, beneficio y ROI estimado.
- Cálculos de eficiencia de Focus cuando existen datos de la receta.
- Clasificación de estrategias según precios y restricciones introducidos por el jugador.

## Ejecución

Requisitos: Python 3.10+; la implementación actual utiliza únicamente la biblioteca estándar de Python.

```bash
python3 main.py
```

El programa solicita plata disponible, reserva deseada, supuestos de Focus/Premium, bono de producción, impuestos, precios de materiales y precios de venta. Puede comparar varias recetas o calcular una poción concreta.

## Supuestos y limitaciones

- Los precios y las tarifas los introduce el usuario; no existe consulta de mercado en tiempo real.
- Las recetas y cantidades son datos locales y pueden necesitar actualización tras los parches del juego.
- Esta versión supone cinco pociones por fabricación.
- El retorno de recursos se modela como valor esperado; el redondeo exacto del juego y algunos valores de receta/Focus todavía requieren validación.
- El beneficio y el ROI son estimaciones, no garantías de resultados de mercado.

---

[Português](./README.pt-BR.md) · [English](./README.md) · [Español](./README.es.md)
