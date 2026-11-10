# Demo tienda

Módulo pequeño que calcula el total de un pedido y aplica cupones de descuento. Sirve para practicar Claude Code.

## Estructura
- `tienda/`: lógica (`precios.py` para cupones, `pedidos.py` para totales).
- `.claude/rules/nombres-funciones.md`: estándar de nombres de funciones (se carga al trabajar en `tienda/`).

## Reglas
- Variables en snake_case.
- Toda función pública de `tienda/` lleva un docstring de una línea.
- Sin números mágicos en la lógica: usar constantes con nombre.
- No usar `print` en `tienda/`: usar el módulo `logging`.

## Qué no hacer
- No leer ni editar `.env`.
- No agregar dependencias externas: solo la biblioteca estándar.
- Si una tarea toca más de 3 archivos, detente y pregunta antes de seguir.
