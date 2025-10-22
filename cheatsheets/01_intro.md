# 📘 Cheat Sheet: Introducción a Python

## 🎯 Conceptos clave

Python es un lenguaje de programación:
- **Interpretado**: se ejecuta línea por línea
- **Dinámicamente tipado**: no necesitas declarar tipos de variables
- **Alto nivel**: sintaxis cercana al lenguaje humano
- **Multiparadigma**: soporta programación imperativa, orientada a objetos y funcional

---

## 🚀 Ejecutar Python

```bash
# Modo interactivo (REPL)
python

# Ejecutar un archivo
python mi_script.py

# Ver versión de Python
python --version
```

---

## 🌍 Entornos virtuales (venv)

### ¿Qué es un entorno virtual?

Un **entorno virtual** es una carpeta aislada que contiene su propia instalación de Python y sus paquetes. Permite trabajar en proyectos diferentes con dependencias distintas sin conflictos.

### ¿Por qué son importantes?

✅ **Aislamiento**: Cada proyecto tiene sus propias dependencias  
✅ **Reproducibilidad**: Puedes compartir exactamente qué versiones usar  
✅ **Limpieza**: No ensucian la instalación global de Python  
✅ **Profesionalismo**: Es el estándar en desarrollo real

### Crear y usar un entorno virtual

```bash
# Crear entorno virtual (se hace una vez por proyecto)
python -m venv .venv

# Activar el entorno
# En Windows PowerShell:
.venv\Scripts\Activate.ps1

# En Windows CMD:
.venv\Scripts\activate.bat

# En macOS/Linux:
source .venv/bin/activate

# Verás (venv) o (.venv) en tu terminal cuando esté activo

# Instalar paquetes (se instalan solo en el entorno)
pip install pytest ruff

# Desactivar el entorno
deactivate
```

### Buenas prácticas

- 📁 **Nombra tu entorno** `.venv` o `venv` (por convención)
- 🚫 **No subas el entorno a Git** (añade `.venv/` a `.gitignore`)
- 📝 **Usa `requirements.txt`** para compartir dependencias:
  ```bash
  # Guardar dependencias
  pip freeze > requirements.txt
  
  # Instalar dependencias de otro proyecto
  pip install -r requirements.txt
  ```

---

## 📝 Variables y asignación

```python
# Asignación simple
nombre = "Ana"
edad = 25
altura = 1.65
es_estudiante = True

# Asignación múltiple
x, y, z = 1, 2, 3

# Mismo valor a múltiples variables
a = b = c = 0
```

### Reglas para nombrar variables
✅ Pueden contener letras, números y guiones bajos  
✅ Deben empezar con letra o guion bajo  
✅ Son case-sensitive (`nombre` ≠ `Nombre`)  
❌ No pueden ser palabras reservadas (`if`, `for`, `class`, etc.)

**Convención**: usa `snake_case` para variables y funciones

---

## 🔢 Tipos de datos básicos

```python
# Enteros (int)
numero = 42
negativo = -10

# Flotantes (float)
precio = 19.99
temperatura = -3.5

# Cadenas (str)
saludo = "Hola"
mensaje = 'Python es genial'
multilinea = """Este es un
texto de varias líneas"""

# Booleanos (bool)
activo = True
completado = False
```

---

## 🔍 Función `type()`

```python
type(42)          # <class 'int'>
type(3.14)        # <class 'float'>
type("Hola")      # <class 'str'>
type(True)        # <class 'bool'>
```

---

## ➗ Operadores aritméticos

```python
suma = 5 + 3           # 8
resta = 10 - 4         # 6
multiplicacion = 3 * 4 # 12
division = 15 / 3      # 5.0 (siempre devuelve float)
division_entera = 15 // 4  # 3 (descarta decimales)
modulo = 17 % 5        # 2 (resto de la división)
potencia = 2 ** 3      # 8 (2 elevado a 3)
```

---

## 📥 Entrada y salida

### Salida con `print()`
```python
print("Hola, mundo")
print("Tengo", 25, "años")

# f-strings: forma moderna de formatear (explicación completa en 02_estructuras.md)
nombre = "Ana"
edad = 25
print(f"Mi nombre es {nombre} y tengo {edad} años")
```

### Entrada con `input()`
```python
nombre = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ")  # Devuelve siempre un string

# Convertir a número
edad = int(input("¿Cuántos años tienes? "))
```

---

## 📄 Comentarios

```python
# Esto es un comentario de una línea

"""
Este es un comentario
de múltiples líneas
(también conocido como docstring)
"""
```

---

## ⚙️ Conversiones de tipo (casting)

```python
# De string a número
num = int("42")       # 42
precio = float("19.99")  # 19.99

# De número a string
texto = str(100)      # "100"

# Booleanos
bool(1)    # True
bool(0)    # False
bool("")   # False
bool("Hola")  # True
```

---

## 🎨 Ejemplos prácticos

### Calculadora de área

```python
# Programa que calcula el área de un rectángulo
print("=== Calculadora de área ===")

base = float(input("Introduce la base: "))
altura = float(input("Introduce la altura: "))

area = base * altura

print(f"El área del rectángulo es: {area}")
```

---

## 🚨 Errores comunes

❌ **Usar una variable sin definirla**
```python
print(nombre)  # NameError: name 'nombre' is not defined
```

❌ **Mezclar tipos incompatibles**
```python
edad = "25"
print(edad + 5)  # TypeError
```
✅ Solución: `print(int(edad) + 5)`

❌ **Olvidar convertir `input()`**
```python
edad = input("Edad: ")  # edad es string
if edad > 18:  # Error: no se puede comparar string con int
```
✅ Solución: `edad = int(input("Edad: "))`

---

## 📌 Conceptos clave

- Python es **interpretado** y **dinámicamente tipado**
- Las variables se declaran simplemente asignando un valor
- Usa **entornos virtuales** para cada proyecto (aislamiento profesional)
- **f-strings** son la forma moderna de formatear texto
- `input()` siempre devuelve un string, usa `int()` o `float()` para convertir
- Los **comentarios** explican el "por qué", no el "qué"
- La indentación NO es opcional, es parte de la sintaxis

### 📚 Recursos adicionales

- [Documentación oficial de Python](https://docs.python.org/es/3/)
- [PEP 8 – Guía de estilo](https://pep8.org/)
- [Real Python - Guías para principiantes](https://realpython.com/)
