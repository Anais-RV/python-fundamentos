# Guía de contribución

Gracias por contribuir a este repositorio pedagógico. Sigue estos pasos precisos para mantener un flujo ordenado.

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
- Cada módulo está en `01_intro` a `07_mini_proyectos` con su `README.md`, `ejercicios.md` y `ejemplos/`.
- No subas soluciones a `main` ni a `revision`.

## Rama `solutions`
- Las soluciones oficiales viven en la rama `solutions`, en carpetas espejo bajo `soluciones/`.
- Cómo verlas sin mezclar:
  1. Añade el remoto del repo original (si aún no lo tienes):
     - `git remote add upstream https://github.com/ORG/python-ejercicios.git`
  2. Trae la rama solutions:
     - `git fetch upstream solutions:solutions`
  3. Explora un archivo puntual sin cambiar de rama:
     - `git show solutions:soluciones/01_intro/ejemplos/hola.py`
  4. Opcional: crea una rama local temporal basada en `solutions` para estudiar:
     - `git switch --detach solutions`

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
