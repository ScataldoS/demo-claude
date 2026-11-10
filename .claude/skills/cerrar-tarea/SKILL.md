---
name: cerrar-tarea
description: Cierra una tarea sobre tienda/ con el flujo revisor, corrector y committer, con una sola vuelta de corrección. Úsalo al terminar de escribir o modificar código en tienda/, antes de dar la tarea por terminada, para dejarlo revisado y guardado en un commit.
---
# Cierre de tarea: revisar, corregir y guardar

Tú coordinas el flujo y lanzas cada agente con la herramienta `Agent`. No edites código ni hagas el commit tú mismo: cada paso lo hace su agente. Hay **una sola vuelta de corrección**: no repitas el ciclo.

## Flujo

1. **Primera revisión.** Lanza `revisor` sobre `tienda/`.
   - Si el informe dice **"Sin incumplimientos"**, salta al paso 4.
   - Si trae hallazgos, sigue con el paso 2.
2. **Corrección.** Lanza `corrector` con el informe completo del `revisor`, tal cual, sin resumirlo.
   - Si el corrector se detuvo (tocaría más de 3 archivos, o el hallazgo ya no coincide con el código), **para el flujo**, muéstrale al usuario lo que informó y pregunta cómo seguir.
3. **Segunda revisión.** Lanza `revisor` otra vez sobre `tienda/`.
   - Si dice **"Sin incumplimientos"**, sigue con el paso 4.
   - Si aún hay hallazgos, **para el flujo**: no hay más vueltas ni commit. Muestra los hallazgos restantes al usuario.
4. **Commit.** Lanza `committer` con un encargo que incluya:
   - el informe del `revisor` con "Sin incumplimientos", pegado completo y sin modificar;
   - la lista de archivos de `tienda/` que debe guardar y una frase con lo que cambió;
   - la aclaración de que cualquier otro cambio del repositorio, fuera de esa lista, no se incluye.
   El commit pide aprobación al usuario: es lo esperado.

## Reglas del flujo
- Nunca escribas "Sin incumplimientos" por tu cuenta ni lo des por hecho: debe venir del informe del `revisor` de esa pasada.
- Si el `committer` rechaza el commit, no lo reintentes: informa su motivo y qué agente debe intervenir.
- `git push` no forma parte del flujo. Lo decide una persona.

## Resumen final para el usuario
- Hallazgos de la primera revisión (cantidad) y qué corrigió el `corrector`.
- Resultado de la segunda revisión.
- Si hubo commit: hash corto y asunto, y que el push queda pendiente.
- Si el flujo se detuvo: en qué paso y por qué.
