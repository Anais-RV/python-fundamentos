# 📁 Guía de Estructura de Trabajo para Estudiantes

Esta guía explica cómo organizar tu trabajo mientras resuelves los ejercicios del curso.

---

## 🎯 Filosofía de organización

- ✅ **Cada módulo = una carpeta de trabajo**
- ✅ **Un archivo por ejercicio**
- ✅ **Nombres descriptivos**
- ✅ **Estructura consistente y predecible**

---

## 📂 Estructura recomendada

```
python-fundamentos/                    ← Tu fork del repositorio
│
├── 01_intro/
│   ├── MODULO.md                     ← Lee primero (objetivos)
│   ├── ejercicios.md                 ← Lista de ejercicios a hacer
│   ├── ejemplos/                     ← Código de referencia (NO modificar)
│   │   └── hola.py
│   ├── ejercicio_guiado/             ← Ejercicio opcional "Calculadora"
│   │   ├── GUIA.md
│   │   └── calculadora_v1.py         ← Completa aquí los TODOs
│   │
│   └── mis_ejercicios/               ← 🎯 TU CARPETA DE TRABAJO
│       ├── 01_primer_script.py       ← Ejercicio guiado 1
│       ├── 02_saludo_input.py        ← Ejercicio guiado 2
│       ├── 03_variables_basicas.py   ← Ejercicio autónomo 1
│       ├── 04_conversor.py           ← Ejercicio autónomo 2
│       ├── 05_tres_prints.py         ← Ejercicio autónomo 3
│       ├── 06_eco.py                 ← Ejercicio autónomo 4
│       └── 07_bigotes_felices.py     ← Desafío
│
├── 02_estructuras/
│   ├── MODULO.md
│   ├── ejercicios.md
│   ├── ejemplos/
│   ├── ejercicio_guiado/
│   │   └── calculadora_v2.py
│   │
│   └── mis_ejercicios/               ← 🎯 TU CARPETA DE TRABAJO
│       ├── 01_operaciones.py
│       ├── 02_casting.py
│       ├── 03_booleans.py
│       └── ...
│
├── 03_control_flujo/
│   └── mis_ejercicios/               ← Mismo patrón en todos los módulos
│       └── ...
│
└── ... (módulos 04-07 siguen el mismo patrón)
```

---

## 🚀 Flujo de trabajo paso a paso

### 1️⃣ Preparación del módulo

```bash
# Entra al módulo que vas a trabajar
cd 01_intro

# Crea tu carpeta de trabajo
mkdir mis_ejercicios
cd mis_ejercicios
```

### 2️⃣ Para cada ejercicio

**Pasos**:

1. **Lee** `ejercicios.md` para saber qué hacer
2. **Crea** un archivo con nombre descriptivo: `01_nombre_ejercicio.py`
3. **Resuelve** el ejercicio en ese archivo
4. **Prueba** ejecutando: `python 01_nombre_ejercicio.py`
5. **Commit** cuando funcione correctamente

**Ejemplo práctico** (Ejercicio "Primer script" del módulo 01):

```python
# Archivo: 01_intro/mis_ejercicios/01_primer_script.py

# Ejercicio: Imprimir un saludo y una variable
nombre = "Ana"
print("Hola, Python")
print(f"Hola, {nombre}")
```

```bash
# Prueba
python 01_primer_script.py

# Si funciona, haz commit
git add 01_primer_script.py
git commit -m "feat: resolver ejercicio 01 - primer script"
```

### 3️⃣ Ejercicio guiado "Calculadora"

Este ejercicio tiene plantilla incluida:

```bash
# NO crees archivo nuevo, trabaja sobre la plantilla
cd 01_intro/ejercicio_guiado

# Abre calculadora_v1.py y completa los TODOs
# La plantilla ya tiene la estructura, solo completas los huecos

# Prueba
python calculadora_v1.py

# Commit
git add calculadora_v1.py
git commit -m "feat: completar calculadora v1 - suma básica"
```

---

## 📝 Convención de nombres de archivos

### ✅ Buenos nombres (descriptivos)

```
✅ 01_primer_script.py        ← Prefijo numérico + descripción
✅ 02_saludo_input.py          ← Sigue orden de ejercicios.md
✅ 03_variables_basicas.py     ← Snake_case (guiones bajos)
✅ 07_bigotes_felices.py       ← Nombre del desafío
```

### ❌ Malos nombres (evitar)

```
❌ ejercicio1.py               ← No descriptivo
❌ test.py                     ← Genérico
❌ prueba_cosas.py             ← Vago
❌ EjercicioUno.py             ← No usar PascalCase para scripts
```

### 💡 Patrón recomendado

```
[numero]_[nombre_descriptivo].py

Donde:
- [numero] = orden del ejercicio en ejercicios.md (01, 02, 03...)
- [nombre_descriptivo] = qué hace el ejercicio (en snake_case)
```

---

## 🔄 Workflow completo de ejemplo

```bash
# 1. Clonar tu fork
git clone https://github.com/TU-USUARIO/python-fundamentos.git
cd python-fundamentos

# 2. Crear rama de trabajo
git checkout -b ejercicios-TuNombre

# 3. Configurar entorno virtual (solo primera vez)
python -m venv .venv
.venv\Scripts\Activate.ps1  # En Windows
pip install -r requirements.txt

# 4. Trabajar en un módulo
cd 01_intro
mkdir mis_ejercicios
cd mis_ejercicios

# 5. Resolver ejercicios (crear archivos uno por uno)
# Crear 01_primer_script.py, resolver, probar, commit
# Crear 02_saludo_input.py, resolver, probar, commit
# ... etc

# 6. Cuando termines el módulo
git push origin ejercicios-TuNombre

# 7. Abrir Pull Request hacia la rama 'revision'
```

---

## 🎓 Ventajas de esta estructura

### ✅ Para ti (estudiante)

- **Organizado**: Cada módulo en su carpeta
- **Claro**: Nombres descriptivos, fácil encontrar ejercicios
- **Profesional**: Simula estructura de proyectos reales
- **Rastreable**: Git muestra claramente qué has hecho
- **No invasivo**: No modificas archivos del curso original

### ✅ Para la revisión

- **Fácil revisar**: Todo en `mis_ejercicios/`
- **Reutilizable**: Plantillas y ejemplos no se tocan
- **Trazabilidad**: Commits claros por ejercicio
- **Comparación**: Fácil ver diferencias con `git diff`

---

## 📋 Checklist por módulo

```markdown
Módulo: 01_intro

- [ ] Leer MODULO.md (objetivos)
- [ ] Leer ejercicios.md (qué hacer)
- [ ] Revisar ejemplos/ (código de referencia)
- [ ] Crear carpeta mis_ejercicios/
- [ ] Resolver ejercicios guiados (01_*, 02_*)
- [ ] Resolver ejercicios autónomos (03_*, 04_*, 05_*, 06_*)
- [ ] Resolver desafío (07_*)
- [ ] (Opcional) Completar ejercicio_guiado/calculadora_v1.py
- [ ] Hacer commits por ejercicio
- [ ] Push y abrir PR
```

---

## 🚫 Qué NO hacer

### ❌ NO modifiques archivos del curso

```
❌ ejemplos/hola.py                  ← NO tocar (son de referencia)
❌ ejercicio_guiado/GUIA.md          ← NO modificar (es la guía)
❌ MODULO.md                         ← NO editar (es del curso)
```

### ❌ NO pongas todo en un solo archivo

```python
❌ todos_los_ejercicios.py           ← Difícil de revisar
❌ ejercicios.py                     ← No específico
```

### ❌ NO uses carpetas anidadas innecesarias

```
❌ mis_ejercicios/
   └── ejercicio1/
       └── main.py                   ← Sobrecomplica
       
✅ mis_ejercicios/
   └── 01_nombre.py                  ← Simple y directo
```

---

## 💡 Tips profesionales

### 1. Usa commits descriptivos

```bash
✅ git commit -m "feat: resolver ejercicio 01 - primer script"
✅ git commit -m "feat: completar ejercicio 03 - variables básicas"
✅ git commit -m "fix: corregir validación en ejercicio bigotes felices"

❌ git commit -m "ejercicio 1"
❌ git commit -m "actualizar"
```

### 2. Prueba antes de hacer commit

```bash
# Siempre ejecuta tu código antes de commit
python mis_ejercicios/01_primer_script.py

# Si usa input, prueba varios casos
python mis_ejercicios/02_saludo_input.py
# Prueba: nombre normal, nombre vacío, caracteres especiales
```

### 3. Consulta el cheatsheet mientras trabajas

```bash
# Mantén abierto el cheatsheet correspondiente
# Ejemplo: mientras haces ejercicios de 02_estructuras:
# Abre en otra ventana: cheatsheets/02_estructuras.md
```

### 4. Compara con ejemplos

```bash
# Si te atascas, revisa los ejemplos del módulo
# Ejemplo: 01_intro/ejemplos/hola.py
```

---

## 🆘 Resolución de problemas

### "No sé cómo nombrar mi archivo"

**Solución**: Usa el nombre del ejercicio en `ejercicios.md` + prefijo numérico

```
Ejercicio en ejercicios.md: "Guiado 1: Tu primer script"
→ Nombre archivo: 01_primer_script.py

Ejercicio: "Autónomo 3: Crea tres_prints.py"
→ Nombre archivo: 03_tres_prints.py
```

### "¿Dónde pongo el desafío?"

**Solución**: En `mis_ejercicios/` con prefijo alto (ej: `07_` si hay 6 ejercicios antes)

### "¿Puedo tener subcarpetas en mis_ejercicios/?"

**Solución**: Solo si son muchos ejercicios (20+). En este curso no es necesario.

---

## 📚 Recursos

- [Guía de Git básico](../docs/guia-git-basico.md) ← (si existe)
- [Convenciones de commits](../CONTRIBUTING.md)
- [Cómo hacer un PR](../docs/checklist-revision-pares.md)

---

**Autor**: Anaïs Rodríguez Villanueva  
**Última actualización**: Octubre 2025

> 💡 Esta estructura es una **recomendación profesional**. Si tienes un sistema que funciona mejor para ti, úsalo. Lo importante es mantener organización y claridad.
