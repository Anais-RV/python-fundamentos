# 🐍 Python Fundamentos

Repositorio pedagógico de ejercicios de Python pensado para estudiantes con base en bases de datos y experiencia previa con GitHub (forks, ramas y PRs). Incluye estructura clara, ejercicios graduados, ejemplos, CI, linting y una guía de contribución precisa.

---

## 📑 Índice

- [🎯 Requisitos](#-requisitos)
- [👤 Flujo de trabajo del alumno](#-flujo-de-trabajo-del-alumno)
- [📝 Normas de commits](#-normas-de-commits)
- [🧪 Cómo ejecutar tests y lint](#-cómo-ejecutar-tests-y-lint)
- [📚 Documentación del repositorio](#-documentación-del-repositorio)
  - [📖 Cheat Sheets de Python](#-cheat-sheets-de-python)
  - [📋 Guías del curso](#-guías-del-curso)
- [📂 Estructura del repositorio](#-estructura-del-repositorio)
- [🗺️ Módulos de aprendizaje](#️-módulos-de-aprendizaje)

---

## 🎯 Requisitos
- Python 3.12 o superior
- Git
- make (opcional pero recomendado para ejecutar tareas locales)

> 💡 **Importante sobre entornos virtuales**: Este proyecto utiliza entornos virtuales (`.venv`) para aislar dependencias. Es una práctica profesional estándar que evita conflictos entre proyectos. Consulta [`cheatsheets/01_intro.md`](./cheatsheets/01_intro.md#-entornos-virtuales-venv) para aprender qué son y por qué son importantes.

## 👤 Flujo de trabajo del alumno
1. Haz un fork de este repositorio en tu cuenta.
2. Clona tu fork localmente.
3. Crea una rama para tus ejercicios: `ejercicios-Nombre` (usa tu nombre o alias).
4. Trabaja con commits pequeños y descriptivos.
5. Abre un Pull Request (PR) desde tu rama `ejercicios-Nombre` hacia la rama `revision` de este repo.
6. Participa en la revisión por pares y atiende comentarios de la formadora.

## 📝 Normas de commits
Prefijos recomendados:
- `feat:` nueva funcionalidad/ejercicio
- `fix:` correcciones
- `refactor:` reestructuración sin cambiar comportamiento
- `test:` pruebas
- `docs:` documentación

Ejemplo: `feat: agregar ejercicios guiados de 01_intro`

## 🧪 Cómo ejecutar tests y lint
Con make:
- `make setup` (crea el entorno y instala dependencias mínimas)
- `make test`
- `make lint`

Sin make (alternativa manual):
 - Windows PowerShell: `python -m venv .venv; .venv/Scripts/Activate.ps1; python -m pip install -U pip ruff pytest`
- macOS/Linux: `python3 -m venv .venv; source .venv/bin/activate; python -m pip install -U pip ruff pytest`
- Ejecutar: `pytest -q` y `ruff check .`

## 📚 Documentación del repositorio

Este repositorio contiene **dos tipos de documentación** con propósitos diferentes:

### 📖 Cheat Sheets de Python

📁 **Carpeta: [`cheatsheets/`](./cheatsheets/)** - Referencia técnica de Python

Hojas de referencia rápida para consultar mientras programas:

| Archivo | Contenido |
|---------|-----------|
| [� INDICE](./cheatsheets/INDICE.md) | Índice y guía de uso de los cheat sheets |
| [01_intro.md](./cheatsheets/01_intro.md) | Variables, tipos básicos, **entornos virtuales** ⭐ |
| [02_estructuras.md](./cheatsheets/02_estructuras.md) | Strings, números, booleanos, **f-strings** ⭐ |
| [03_control_flujo.md](./cheatsheets/03_control_flujo.md) | if/elif/else, for, while, break/continue |
| [04_funciones.md](./cheatsheets/04_funciones.md) | Definición, parámetros, return, scope, lambdas |
| [05_colecciones.md](./cheatsheets/05_colecciones.md) | Listas, tuplas, diccionarios, sets |
| [06_archivos_y_modulos.md](./cheatsheets/06_archivos_y_modulos.md) | I/O archivos, imports, JSON/CSV |
| [🚀 python_quick_reference.md](./cheatsheets/python_quick_reference.md) | **Referencia rápida todo-en-uno** |

💡 **Tip**: Mantén abierto `python_quick_reference.md` mientras programas.

### 📋 Guías del curso

📁 **Carpeta: [`docs/`](./docs/)** - Organización pedagógica

Documentación sobre cómo está estructurado el curso:

| Archivo | Contenido |
|---------|-----------|
| [roadmap.md](./docs/roadmap.md) | Ruta de aprendizaje y tiempos estimados |
| [rubrica-evaluacion.md](./docs/rubrica-evaluacion.md) | Criterios de evaluación |
| [checklist-revision-pares.md](./docs/checklist-revision-pares.md) | Guía para revisión por pares |

---

## 📂 Estructura del repositorio

```
python-fundamentos/
├─ 01_intro/                → primeros pasos con Python
├─ 02_estructuras/          → tipos básicos y operadores
├─ 03_control_flujo/        → condicionales y bucles
├─ 04_funciones/            → funciones y parámetros
├─ 05_colecciones/          → listas, tuplas, diccionarios, sets
├─ 06_archivos_y_modulos/   → manejo de archivos e imports
├─ 07_mini_proyectos/       → pequeños retos aplicados
├─ cheatsheets/             → � referencia rápida de Python (sintaxis, ejemplos)
├─ docs/                    → 📋 guías del curso (roadmap, rúbricas)
└─ tests/                   → pruebas automáticas con pytest
```

---

## 🗺️ Módulos de aprendizaje

Cada módulo contiene:
- 📖 **README.md** - Objetivos y conceptos clave
- 📝 **ejercicios.md** - Ejercicios guiados y autónomos
- 💻 **ejemplos/** - Código de ejemplo ejecutable

### Ruta sugerida

1. **[01_intro](./01_intro/)** - Primeros pasos
   - Variables, tipos básicos, entrada/salida
   - ⚠️ **Configura tu entorno virtual aquí**
   
2. **[02_estructuras](./02_estructuras/)** - Tipos de datos
   - Strings, números, booleanos, conversiones
   - 📚 Aprende f-strings (muy importante)
   
3. **[03_control_flujo](./03_control_flujo/)** - Decisiones y repeticiones
   - if/elif/else, for, while
   
4. **[04_funciones](./04_funciones/)** - Organización del código
   - Definir funciones, parámetros, return
   
5. **[05_colecciones](./05_colecciones/)** - Estructuras de datos
   - Listas, tuplas, diccionarios, sets
   
6. **[06_archivos_y_modulos](./06_archivos_y_modulos/)** - Persistencia y organización
   - Leer/escribir archivos, imports
   
7. **[07_mini_proyectos](./07_mini_proyectos/)** - Aplicación práctica
   - Proyectos integradores

---

## 🎓 Próximos pasos

1. ✅ Lee el [roadmap](./docs/roadmap.md) para entender la estructura del curso
2. ✅ Configura tu entorno según [`cheatsheets/01_intro.md`](./cheatsheets/01_intro.md)
3. ✅ Haz un fork del repositorio
4. ✅ Empieza con [`01_intro/ejercicios.md`](./01_intro/ejercicios.md)
5. ✅ Mantén abierta la [referencia rápida](./cheatsheets/python_quick_reference.md)

**¡Feliz aprendizaje! 🚀**

---

## 👥 Créditos

**Autoría y diseño pedagógico**: Anaïs Rodríguez Villanueva

Este material ha sido desarrollado con fines educativos como parte de un programa de formación en desarrollo web e inteligencia artificial.

### 📄 Licencia

Este proyecto está bajo licencia MIT. Puedes reutilizar y adaptar el material citando la autoría original.

### 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, consulta [CONTRIBUTING.md](./CONTRIBUTING.md) para más detalles sobre cómo participar en el proyecto.
