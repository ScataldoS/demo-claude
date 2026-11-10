---
name: revisar-corregir
description: Revisa tienda/ contra los estándares con el revisor, aplica los hallazgos con el corrector y vuelve a revisar, con una sola vuelta de corrección y sin commit.
disable-model-invocation: true
---
# Revisar y corregir, sin commit

Tú coordinas el flujo y lanzas cada agente con la herramienta `Agent`. No edites código tú mismo: cada paso lo hace su agente. Hay **una sola vuelta de corrección**: no repitas el ciclo. **No hagas commit** ni lances `committer`: para guardar está `/cerrar-tarea`.

## Flujo

1. **Primera revisión.** Lanza `revisor` sobre `tienda/`.
   - Si el informe dice **"Sin incumplimientos"**, termina y pasa al resumen final.
   - Si trae hallazgos, sigue con el paso 2.
2. **Corrección.** Lanza `corrector` con el informe completo del `revisor`, tal cual, sin resumirlo.
   - Si el corrector se detuvo (tocaría más de 3 archivos, o el hallazgo ya no coincide con el código), **para el flujo**, muéstrale al usuario lo que informó y pregunta cómo seguir.
3. **Segunda revisión.** Lanza `revisor` otra vez sobre `tienda/`.
   - Si aún hay hallazgos, **para el flujo**: no hay más vueltas. Muestra los hallazgos restantes al usuario.

## Reglas del flujo
- Nunca escribas "Sin incumplimientos" por tu cuenta ni lo des por hecho: debe venir del informe del `revisor` de esa pasada.
- No hagas commit ni `git push`.

## Resumen final para el usuario
- Hallazgos de la primera revisión (cantidad) y qué corrigió el `corrector`.
- Resultado de la segunda revisión.
- Archivos modificados, que quedan sin commit.
- Si el flujo se detuvo: en qué paso y por qué.
