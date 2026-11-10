---
name: revision-estandares
description: Procedimiento para revisar el código de tienda/ contra los estándares de codificación del proyecto, con foco en el nombramiento de funciones, y entregar un informe de hallazgos. Úsalo al revisar archivos antes de dar una tarea por terminada.
---
# Revisión de estándares de codificación

Los estándares viven en dos archivos: el **estándar de nombres de funciones** en `.claude/rules/nombres-funciones.md` y las **reglas** en `CLAUDE.md`. Léelos con Read antes de revisar y revisa contra su texto actual, no contra lo que recuerdes de ellos.

## Nombres de funciones
Lista todas las funciones con Grep (`^\s*def \w+`) y revisa cada nombre contra los cuatro puntos del estándar.

| Punto del estándar | Cómo detectar el incumplimiento |
| --- | --- |
| 1. snake_case en minúsculas | El nombre tiene una mayúscula: `def [a-z_0-9]*[A-Z]`. |
| 2. Verbo en infinitivo + objeto | El primer segmento (hasta el primer `_`) debe ser un verbo que termine en `ar`, `er` o `ir`, y debe haber un objeto después. Un nombre sin `_`, o que empieza con un sustantivo (`resumen_pedido`, `total`), es hallazgo. Confirma que sea un verbo y no solo que termine así. Excepción: las booleanas del punto 3. |
| 3. Booleanas con `es_`, `tiene_` o `puede_` | Una función cuyo `return` es un booleano o una comparación debe empezar con uno de esos prefijos. Y al revés: una función con ese prefijo debe devolver un booleano. |
| 4. Sin genéricos ni abreviaturas | Compara con la lista del estándar (`procesar`, `manejar`, `hacer`, `datos`) y busca segmentos de tres letras o menos que abrevien una palabra (`calc_tot`). |

En cada hallazgo de nombres, la sugerencia incluye el **nombre correcto propuesto**.

## Reglas del CLAUDE.md

| Regla | Cómo detectar el incumplimiento |
| --- | --- |
| Variables en snake_case | Busca con Grep asignaciones y parámetros con mayúsculas, por ejemplo `\b[a-z]+[A-Z]\w*\s*=`. |
| Docstring de una línea | Toda `def` pública (sin `_` inicial) debe tener una cadena de una línea justo debajo. Falta o ocupa varias líneas: hallazgo. |
| Sin números mágicos | Un literal numérico distinto de 0 y 1, usado dentro de una expresión de la lógica en lugar de una constante con nombre: hallazgo. La definición de la propia constante no lo es. |
| Sin `print` | Busca `print\(` con Grep en `tienda/`. Cada coincidencia es un hallazgo. |

## Cómo trabajar
1. Lee `.claude/rules/nombres-funciones.md` y `CLAUDE.md`.
2. Lista los archivos con Glob y lee cada uno completo. Usa Grep para no saltarte coincidencias.
3. Revisa regla por regla en todos los archivos, no archivo por archivo.
4. Anota solo lo que viste en el código, con su número de línea real. No supongas.

## Informe
Una línea por hallazgo, ordenadas por archivo y línea:

`archivo:línea · regla incumplida · sugerencia breve`

Cierra con el total de hallazgos. Si no hay ninguno, escribe de forma explícita **"Sin incumplimientos"** y las reglas que revisaste.

No modifiques nada ni propongas cambios fuera de los hallazgos.
