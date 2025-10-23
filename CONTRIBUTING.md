# Guía de contribución

Gracias por contribuir a este repositorio pedagógico. Sigue estos pasos precisos para mantener un flujo ordenado.

## 📝 Sobre las contribuciones

Este proyecto fue creado por **Anaïs Rodríguez Villanueva** de forma independiente y vocacional. Al contribuir:
- ✅ Tu contribución se licenciará bajo los mismos términos (MIT)
- ✅ La autoría original del proyecto se mantiene como Anaïs Rodríguez Villanueva
- ✅ Las contribuciones significativas serán reconocidas en este documento
- ✅ Aceptas que tu contribución puede ser modificada o eliminada si es necesario para mantener la coherencia pedagógica

### Tipos de contribuciones bienvenidas
- 🐛 Corrección de errores (typos, bugs en código de ejemplo)
- 📚 Mejoras en documentación o claridad de ejercicios
- ✨ Nuevos ejercicios o ejemplos complementarios
- 🧪 Tests adicionales
- 💡 Sugerencias pedagógicas

**No se aceptan**:
- ❌ Cambios que eliminen o modifiquen la atribución de autoría
- ❌ Forks que pretendan comercializar el material sin atribución
- ❌ Contribuciones que violen los principios educativos del proyecto

## Flujo de trabajo recomendado
1. Haz fork del repo en GitHub.
2. Clona tu fork localmente.
3. Crea una rama de trabajo por alumno:
   - `git switch -c ejercicios-Nombre`
4. Trabaja con commits pequeños y descriptivos:
   - Añade cambios de forma interactiva: `git add -p`
   - Confirma: `git commit -m "feat: descripcion breve"`
5. Sube tu rama a tu fork:
   - `git push -u origin ejercicios-Nombre`
6. Abre un Pull Request (PR) desde `ejercicios-Nombre` hacia la rama `revision` de este repo.

## Política de revisión
- Primero pasa por la checklist de pares (`docs/checklist-revision-pares.md`).
- Luego la formadora hará una revisión final.
- Integra cambios solicitados con commits adicionales (no hagas force push salvo que se te pida).

## Convenciones de estilo
- PEP 8 resumido: 4 espacios de indentación, líneas ≤ 100 caracteres.
- Usa f-strings para formatear strings: `f"Hola, {nombre}"`.
- Nombres claros: `total_gatos`, `promedio_edad`.
- Evita magia: comenta lo necesario y prioriza legibilidad.

## Estructura de carpetas
- Cada módulo está en `01_intro` a `07_mini_proyectos` con su `MODULO.md`, `ejercicios.md` y `ejemplos/`.
- No subas soluciones a `main` ni a `revision`.

## Rama `solutions`
- Las soluciones oficiales viven en la rama `solutions`, en carpetas espejo bajo `soluciones/`.
- Cómo verlas sin mezclar:
  1. Si trabajas en tu fork, añade el remoto del repo original (sólo una vez):
     - `git remote add upstream <URL-del-repo-original>`
  2. Trae la rama solutions desde el remoto que corresponda (tu fork u upstream):
     - `git fetch origin solutions:solutions` (si tu fork ya la tiene)
     - o `git fetch upstream solutions:solutions`
  3. Ver un archivo puntual sin cambiar de rama:
     - `git show solutions:soluciones/01_intro/ejemplos/hola.py`
  4. Opcional: crear una rama local temporal para explorar sin mezclar:
     - `git switch --detach solutions`
  5. Importante: no mezcles `solutions` en `main` ni `revision`. Úsala sólo como referencia.

## Comandos útiles
- Crear entorno e instalar deps: `make setup`
- Lint: `make lint`
- Formato: `make format`
- Tests: `make test`

## Pull Requests
Antes de abrir tu PR, verifica:
- Lint sin errores (ruff)
- Tests pasando (pytest)
- Descripción clara del cambio y aprendizaje
- Capturas o ejemplos de ejecución (opcional)
