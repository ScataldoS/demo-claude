# Guion de la demo

Dura unos 15 minutos. Cada paso muestra una idea de la guía.

## Antes de empezar
1. Abre **esta carpeta** (`demo-claude`) en VS Code y abre Claude Code en ella.
2. El repositorio ya está creado, con un commit `base` marcado con el tag `base`. Sirve para mostrar diffs, `/rewind` y el paso 7.

Lo que el proyecto esconde: un bug en el cálculo de cupones (`PROMO10` sobre 100 da 99.9 en vez de 90) y varias infracciones de los estándares del proyecto en `tienda/pedidos.py`.

Hay dos agentes: `revisor` (revisa estándares de codificación y solo lee) y `committer` (guarda el trabajo en git una vez revisado).

El estándar de nombres de funciones está en `.claude/rules/nombres-funciones.md`, una regla por ruta que aplica a `tienda/`. El resto de las reglas está en `CLAUDE.md`.

---

## Paso 1. Entender sin modificar (modo plan)
Activa el **modo plan** y pide:

> Explica cómo funciona el módulo `tienda/`: entradas, salidas y dependencias. No modifiques nada.

**Qué se ve:** Claude lee el código y explica. No edita nada, y cualquier edición queda bloqueada hasta que la apruebes.

## Paso 2. Pedido vago contra pedido completo
Primero un pedido vago: *"Arregla los cupones"*. Claude tendrá que adivinar qué falla.

Luego, el pedido completo:

> Un pedido con subtotal 100 y el cupón `PROMO10` devuelve 99.9 en lugar de 90. Corrígelo en `tienda/precios.py` para que el descuento sea un porcentaje del subtotal. Comprueba que `calcular_total` da 90 para ese caso. No toques otros archivos.

**Qué se ve:**
- Con el pedido completo Claude sabe qué archivo tocar, qué resultado esperar y cómo comprobarlo. Con el vago tiene que adivinar.
- Edita solo `tienda/precios.py`.
- Si ejecuta Python para comprobar el resultado, pide permiso: ese comando no está en `allow`.

## Paso 3. El que revisa no es quien hizo el trabajo
> Usa el agente `revisor` para revisar `tienda/` contra los estándares del proyecto. Lista cada incumplimiento con archivo y línea.

**Qué debería encontrar** (todo en `tienda/pedidos.py`):
- `resumenPedido` no está en snake_case y no empieza con un verbo en infinitivo (propone `resumir_pedido`).
- `resumenPedido` no tiene docstring.
- `totalFinal` no está en snake_case.
- Usa `print` en vez de `logging`.

También puede señalar números mágicos (`/ 100`, `round(..., 2)`), que incumplen la regla correspondiente.

**Qué se ve:**
- El `revisor` solo tiene `Read`, `Glob` y `Grep`, así que no puede modificar nada. Está en `tools:` de su `.md`.
- Revisa contra `CLAUDE.md` y `.claude/rules/nombres-funciones.md`, que son la única fuente de los estándares, y sigue el procedimiento de su skill `revision-estandares`.

## Paso 4. Aplicar los hallazgos y deshacer
Pide que corrija los hallazgos del paso 3, y después prueba `/rewind` para volver al estado anterior.

**Qué se ve:** quien aprueba el cambio es responsable de él, y siempre se puede volver atrás.

## Paso 5. Permisos
Pide cada una por separado:

| Pedido | Resultado esperado |
| --- | --- |
| "Lee el archivo `.env`" | Bloqueado por `deny` |
| "Haz `git push --force`" | Bloqueado por `deny` |
| "Haz `git push`" | Pide aprobación (`ask`) |

**Para comentar:** `deny: Read(./.env)` se aplica a las herramientas de archivos de Claude. La documentación no asegura que cubra un comando de terminal como `cat .env`, y para una protección que no dependa del texto del comando recomienda usar sandboxing. Los permisos se diseñan, no se asumen.

## Paso 6. Sesiones y contexto
Ejecuta `/context` para ver qué ocupa espacio y termina con `/clear` al cambiar de tarea.

**Qué se ve:** una sesión por tarea. Lo que debe sobrevivir entre sesiones está en `CLAUDE.md`.

## Paso 7. Cerrar con commit
Con los hallazgos del paso 3 corregidos, pide:

> Pasa el agente `revisor` por `tienda/`. Si no hay incumplimientos, usa el agente `committer` para guardar el trabajo.

**Qué se ve:**
- El `committer` exige el informe del `revisor` con "Sin incumplimientos" y lo contrasta con dos búsquedas propias en `tienda/` (`print` y nombres en camelCase). No puede lanzar al `revisor` (un agente no lanza a otros), así que el orden lo da tu conversación.
- Solo tiene `Read`, `Glob`, `Grep` y `Bash`: no puede editar código, solo guardarlo.
- `git commit` está en `ask`: una persona aprueba el commit. El agente nunca hace `git push`.
- Variante: si no corregiste los hallazgos del paso 3 (o hiciste `/rewind`), el `committer` se niega y dice qué agente debe volver a actuar.

---

## Para volver a empezar
Restaura el estado inicial con `git reset --hard base` y `git clean -fd`. Esto descarta los cambios sin confirmar, los commits posteriores a `base` y los archivos nuevos. `git reset --hard` está en `deny` para Claude, así que ejecútalo tú en la terminal.
