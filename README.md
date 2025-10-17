# 🐍 Python Fundamentos

> Ejercicios guiados y prácticos para aprender los fundamentos de **Python** — incluye guía paso a paso, flujo GitHub real *(fork → rama → PR)* y comprobaciones automáticas con lint y tests.

---

## 🎯 Objetivo
Este repositorio te acompaña en tus primeros pasos con Python, siguiendo un enfoque **profesional y pedagógico**. Aprenderás a escribir código limpio, estructurado y probado mientras practicas el flujo de trabajo real de un desarrollador con Git y GitHub.

---

## 🧭 Flujo de trabajo

1. **Fork** de este repositorio a tu cuenta.
2. **Clona** tu fork y crea una rama para tus ejercicios:
   ```bash
   git clone <tu-fork>
   cd python-fundamentos
   git switch -c ejercicios-TuNombre
   ```
3. Activa tu entorno y prepara las dependencias:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate   # Windows
   pip install -U pip pytest ruff
   ```
4. Trabaja por bloques (01 → 06) y haz commits pequeños y descriptivos.
5. Abre una Pull Request hacia la rama `revision` del repo original.
6. Espera el ✅ del CI antes de solicitar revisión.

---

## 🧰 Requisitos técnicos

- **Python 3.12 o superior**
- **Git**
- **make** (opcional, pero recomendado para automatizar tareas locales)

### Comandos disponibles si tienes `make`:
```bash
make setup   # crea entorno e instala dependencias
make lint    # revisión de estilo con Ruff
make test    # ejecuta tests automáticos con Pytest
```

### Alternativa manual:
```bash
python -m venv .venv
source .venv/bin/activate      # o .venv\Scripts\activate en Windows
pip install -U pip ruff pytest
pytest -q
ruff check .
```

---

## 📂 Estructura del repositorio

```plaintext
python-fundamentos/
├─ 01_intro/                → primeros pasos con Python
├─ 02_estructuras/          → tipos básicos y operadores
├─ 03_control_flujo/        → condicionales y bucles
├─ 04_funciones/            → funciones y parámetros
├─ 05_colecciones/          → listas, tuplas, diccionarios, sets
├─ 06_archivos_y_modulos/   → manejo de archivos e imports
├─ 07_mini_proyectos/       → pequeños retos aplicados
├─ tests/                   → pruebas automáticas con pytest
└─ docs/                    → guías, rúbrica y checklist
```

---

## 🧠 Cómo trabajar los ejercicios

Cada carpeta contiene:

- **Ejercicios guiados** con pasos numerados.
- **Ejercicios autónomos** para practicar.
- **Un desafío contextualizado** (por ejemplo, Bigotes Felices).
- **Sección de Errores comunes** y **Tiempo estimado**.

Consulta `docs/roadmap.md` para ver el orden sugerido y los objetivos de aprendizaje de cada módulo.

---

## ✍️ Convenciones de commits

Prefijos recomendados:

- `feat:` nueva funcionalidad o ejercicio
- `fix:` corrección de errores
- `refactor:` mejora sin cambio funcional
- `test:` añadidos o ajustes en pruebas
- `docs:` cambios en documentación

Ejemplo:
```bash
git commit -m "feat(intro): completar ejercicio 3 sobre variables"
```

---

## 🧩 Verificación rápida

Antes de subir tu código, asegúrate de que todo pasa correctamente:
```bash
ruff check .
pytest -q
```
Si ambos comandos terminan sin errores, el CI aprobará tu PR automáticamente.

---

## 🪶 Licencia

📄 MIT License — este material puede reutilizarse con fines educativos citando la autoría de la desarrolladora: Anaïs Rodríguez Villanueva.

---

## 💡 Créditos

Desarrollado con fines pedagógicos y vocación docente por **Anaïs Rodríguez Villanueva**, en tiempo personal, como recurso abierto para el aprendizaje de Python.  
El contenido se ofrece bajo licencia **MIT**, permitiendo su uso educativo libre con el debido reconocimiento de autoría.
