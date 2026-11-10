---
name: convencion-commits
description: Condiciones previas y convención de mensajes para hacer un commit en este repo. Úsalo al guardar un trabajo que ya pasó la revisión de estándares.
---
# Commit de un trabajo terminado

## Condiciones previas
Comprueba las cuatro. Si una falla, no hagas el commit.

| Condición | Cómo comprobarla |
| --- | --- |
| Revisión sin incumplimientos | El encargo debe traer el informe del `revisor` con **"Sin incumplimientos"**. Tú no lo lanzas (no tienes la herramienta `Agent`, a propósito): si el informe falta o trae hallazgos, rechaza y pide que se ejecute `revisor`. |
| El informe no está desfasado | Contrástalo tú con dos búsquedas con Grep en `tienda/`: `print\(` y `def [a-z_0-9]*[A-Z]`. No deben dar coincidencias. Si dan alguna, el código cambió después de la revisión o esta fue incompleta: rechaza. |
| Hay cambios que guardar | `git status --short` debe mostrar cambios. Si no hay nada, no hagas commit y dilo. |
| Los cambios son los esperados | Lee `git diff`. Debe coincidir con lo descrito en el encargo. Si aparece `.env`, `__pycache__/` o un cambio que nadie mencionó, detente y avisa. |

## Hacer el commit
1. Prepara los archivos uno por uno, por su ruta: `git add tienda/pedidos.py`. Nunca uses `git add .`, `git add -A` ni `git commit -a`.
2. Revisa lo preparado con `git diff --staged --stat`.
3. Haz el commit con varios `-m`, uno por párrafo: `git commit -m "asunto" -m "cuerpo" -m "Co-Authored-By: ..."`. El commit pide aprobación a una persona: es lo esperado.
4. Comprueba el resultado con `git log -1 --stat`.

## Mensaje
- **Asunto:** `tipo: resumen` en español e imperativo, hasta 72 caracteres y sin punto final. Tipos: `fix`, `feat`, `refactor`, `docs`, `chore`.
- **Cuerpo:** qué cambió y por qué, no cómo. Indica que el `revisor` no halló incumplimientos.
- **Última línea:** `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`

Ejemplo:

    refactor: renombrar resumenPedido a resumir_pedido

    La función incumplía el estándar de nombres: usaba camelCase y no
    empezaba con un verbo en infinitivo. También se agrega su docstring
    y se reemplaza print por logging.
    Revisión: sin incumplimientos.

    Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>

## Lo que nunca haces
`git push`, `--amend`, `reset`, `--force`, `--no-verify`, cambiar la configuración de git y editar archivos.

## Informe
- Hash corto y asunto del commit.
- Archivos incluidos.
- Resultado de las dos búsquedas de contraste.
- Recordatorio de que el push queda pendiente y lo decide una persona.
