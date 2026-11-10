---
name: revisar-corregir-commit
description: Revisa tienda/ contra los estándares con el revisor, aplica los hallazgos con el corrector, vuelve a revisar y, si queda limpio, guarda el trabajo en un commit con el committer. Una sola vuelta de corrección.
disable-model-invocation: true
---
# Revisar, corregir y guardar en un commit

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
4. **Commit.** Si no hay archivos de `tienda/` modificados, no hay nada que guardar: omite este paso. Si los hay, lanza `committer` con un encargo que incluya:
   - el informe del `revisor` con "Sin incumplimientos", pegado completo y sin modificar;
   - la lista de archivos de `tienda/` que debe guardar y una frase con lo que cambió;
   - la aclaración de que cualquier otro cambio del repositorio, fuera de esa lista, no se incluye.
   El commit pide aprobación al usuario: es lo esperado.

## Reglas del flujo
- Nunca escribas "Sin incumplimientos" por tu cuenta ni lo des por hecho: debe venir del informe del `revisor` de esa pasada.
- Si el `committer` rechaza el commit, no lo reintentes: informa su motivo y qué agente debe intervenir.
- `git push` no forma parte del flujo. Lo decide una persona.

## Resumen final para el usuario

Usa siempre este formato, con las mismas secciones y en este orden. No agregues otras secciones ni repitas los informes completos de los agentes. Los archivos van como enlaces markdown con ruta relativa, por ejemplo `[pedidos.py:13](tienda/pedidos.py#L13)`.

```markdown
## Resultado de /revisar-corregir-commit: <Guardado | Sin cambios | Con hallazgos pendientes | Detenido>

**1. Primera revisión:** <N> hallazgos.
| Archivo:línea | Regla | Hallazgo |
| --- | --- | --- |
| <enlace> | <regla> | <qué incumple, en una frase> |

**2. Corrección:** <qué cambió el corrector, una línea por cambio, con enlace>

**3. Segunda revisión:** <"Sin incumplimientos" o N hallazgos, con la misma tabla>

**4. Commit:** <hash corto y asunto, más "push pendiente">

**Archivos guardados:** <lista de enlaces>
```

Reglas del formato:
- Si la primera revisión no trae hallazgos, escribe "0 hallazgos", omite la tabla y pon "No aplica" en los pasos 2 y 3.
- Si no había archivos de `tienda/` modificados, el título dice "Sin cambios", el paso 4 dice "Nada que guardar" y los archivos guardados, "Ninguno".
- Si el flujo se detuvo o el `committer` rechazó el commit, el título dice "Detenido" (o "Con hallazgos pendientes" si fue por la segunda revisión), los pasos que no se hicieron dicen "No se ejecutó", los archivos guardados dicen "Ninguno" y al final se añade `**Motivo de la parada:**` con el paso y la causa, más la pregunta al usuario si el corrector la requiere.
- El estado del título sale del informe del `revisor` de la última pasada y de la respuesta del `committer`, nunca de tu propia valoración.
