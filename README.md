# python-ejercicios

Repositorio pedagógico de ejercicios de Python pensado para estudiantes con base en bases de datos y experiencia previa con GitHub (forks, ramas y PRs). Incluye estructura clara, ejercicios graduados, ejemplos, CI, linting y una guía de contribución precisa.

## Requisitos
- Python 3.12 o superior
- Git
- make (opcional pero recomendado para ejecutar tareas locales)

## Flujo de trabajo del alumno
1. Haz un fork de este repositorio en tu cuenta.
2. Clona tu fork localmente.
3. Crea una rama para tus ejercicios: `ejercicios-Nombre` (usa tu nombre o alias).
4. Trabaja con commits pequeños y descriptivos.
5. Abre un Pull Request (PR) desde tu rama `ejercicios-Nombre` hacia la rama `revision` de este repo.
6. Participa en la revisión por pares y atiende comentarios de la formadora.

## Normas de commits
Prefijos recomendados:
- `feat:` nueva funcionalidad/ejercicio
- `fix:` correcciones
- `refactor:` reestructuración sin cambiar comportamiento
- `test:` pruebas
- `docs:` documentación

Ejemplo: `feat: agregar ejercicios guiados de 01_intro`

## Cómo ejecutar tests y lint
Con make:
- `make setup` (crea el entorno y instala dependencias mínimas)
- `make test`
- `make lint`

Sin make (alternativa manual):
 - Windows PowerShell: `python -m venv .venv; .venv/Scripts/Activate.ps1; python -m pip install -U pip ruff pytest`
- macOS/Linux: `python3 -m venv .venv; source .venv/bin/activate; python -m pip install -U pip ruff pytest`
- Ejecutar: `pytest -q` y `ruff check .`

## Estructura general
Consulta `docs/roadmap.md` y los `README.md` de cada módulo para el orden sugerido y objetivos.
