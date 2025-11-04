# 🚀 Python Quick Reference - Referencia Rápida

Una guía compacta con todo lo esencial de Python en un solo lugar.

---

## 📦 Tipos de datos básicos

```python
# Números
entero = 42
flotante = 3.14
complejo = 2 + 3j

# Texto
texto = "Hola"
multilinea = """Varias
líneas"""

# Booleanos
verdadero = True
falso = False

# None (nulo)
vacio = None
```

---

## 🔤 Strings

```python
# Operaciones
"Hola" + " mundo"       # Concatenar
"Ja" * 3                # Repetir: "JaJaJa"
texto[0]                # Primer carácter
texto[-1]               # Último carácter
texto[1:4]              # Slicing
len(texto)              # Longitud

# Métodos
texto.lower()           # minúsculas
texto.upper()           # MAYÚSCULAS
texto.strip()           # quitar espacios
texto.split(",")        # dividir en lista
texto.replace("a", "x") # reemplazar
texto.startswith("Ho")  # True/False
"a" in texto            # pertenencia

# F-strings
nombre = "Ana"
f"Hola, {nombre}"       # "Hola, Ana"
f"{3.14159:.2f}"        # "3.14" (2 decimales)
```

---

## 🔢 Operadores

```python
# Aritméticos
+  -  *  /              # suma, resta, multiplicación, división
//                      # división entera
%                       # módulo (resto)
**                      # potencia

# Comparación
==  !=  >  <  >=  <=

# Lógicos
and  or  not

# Asignación
=  +=  -=  *=  /=

# Pertenencia
in  not in
```

---

## 🔀 Control de flujo

```python
# If-elif-else
if condicion:
    pass
elif otra_condicion:
    pass
else:
    pass

# Ternario
valor = "mayor" if edad >= 18 else "menor"

# For
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for elem in lista:
    print(elem)

for i, elem in enumerate(lista):
    print(i, elem)

# While
while condicion:
    pass

# Control
break       # sale del bucle
continue    # siguiente iteración
```

---

## 📋 Listas

```python
# Crear
lista = [1, 2, 3]
lista = list(range(5))      # [0, 1, 2, 3, 4]

# Acceso
lista[0]                    # primer elemento
lista[-1]                   # último elemento
lista[1:3]                  # slicing

# Modificar
lista.append(4)             # añadir al final
lista.insert(0, "inicio")   # insertar en posición
lista.extend([5, 6])        # añadir varios
lista.remove(3)             # eliminar valor
elem = lista.pop()          # eliminar y devolver último
del lista[0]                # eliminar por índice

# Métodos
len(lista)                  # longitud
lista.sort()                # ordenar in-place
lista.reverse()             # invertir
lista.count(2)              # contar ocurrencias
lista.index(3)              # índice de valor
3 in lista                  # pertenencia

# Comprehension
[x**2 for x in range(5)]    # [0, 1, 4, 9, 16]
[x for x in nums if x % 2 == 0]  # filtrar pares
```

---

## 🔒 Tuplas

```python
# Crear (inmutables)
tupla = (1, 2, 3)
una = (5,)                  # tupla de 1 elemento

# Desempaquetar
x, y, z = tupla
```

---

## 🗂️ Diccionarios

```python
# Crear
d = {"clave": "valor", "edad": 25}
d = dict(nombre="Ana", edad=25)

# Acceso
d["clave"]
d.get("clave", "default")

# Modificar
d["nueva"] = "valor"
d.update({"k": "v"})
del d["clave"]
d.pop("edad")

# Métodos
d.keys()                    # claves
d.values()                  # valores
d.items()                   # pares (clave, valor)
"clave" in d                # verificar existencia

# Iterar
for clave, valor in d.items():
    print(clave, valor)

# Comprehension
{x: x**2 for x in range(5)}
```

---

## 🎲 Sets

```python
# Crear (sin duplicados)
s = {1, 2, 3}
s = set([1, 2, 2, 3])       # {1, 2, 3}

# Modificar
s.add(4)
s.remove(2)
s.discard(10)               # no error si no existe

# Operaciones
a | b                       # unión
a & b                       # intersección
a - b                       # diferencia
a ^ b                       # diferencia simétrica
```

---

## 🔧 Funciones

```python
# Definir
def funcion(param1, param2="default"):
    """Docstring"""
    return resultado

# Llamar
funcion(1, 2)
funcion(param2=2, param1=1)  # argumentos con nombre

# Args variables
def sumar(*args):           # tupla
    return sum(args)

def mostrar(**kwargs):      # diccionario
    for k, v in kwargs.items():
        print(k, v)

# Lambda
cuadrado = lambda x: x**2
sorted(lista, key=lambda x: len(x))
```

---

## 📂 Archivos

```python
# Leer
with open("archivo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()         # todo
    lineas = f.readlines()       # lista de líneas
    for linea in f:              # línea por línea
        print(linea.strip())

# Escribir
with open("archivo.txt", "w", encoding="utf-8") as f:
    f.write("texto\n")
    f.writelines(["línea1\n", "línea2\n"])

# Append
with open("archivo.txt", "a") as f:
    f.write("nuevo\n")

# JSON
import json
datos = json.load(f)             # leer
json.dump(datos, f, indent=2)    # escribir

# CSV
import csv
lector = csv.reader(f)
escritor = csv.writer(f)
```

---

## 📦 Módulos

```python
# Importar
import modulo
import modulo as m
from modulo import funcion
from modulo import *

# Módulos útiles
import os                   # sistema operativo
import sys                  # sistema Python
import math                 # matemáticas
import random               # aleatorios
import datetime             # fechas
import json                 # JSON
import csv                  # CSV
from pathlib import Path    # rutas
```

---

## 🛠️ Funciones útiles

```python
# Conversiones
int("42")
float("3.14")
str(100)
bool(1)
list("abc")
tuple([1, 2])
set([1, 2, 2])

# Utilidades
len(objeto)                 # longitud
type(objeto)                # tipo
range(5)                    # 0, 1, 2, 3, 4
enumerate(lista)            # índice y elemento
zip(lista1, lista2)         # combinar
sorted(lista)               # ordenar (nueva lista)
reversed(lista)             # invertir
sum([1, 2, 3])              # suma
max(lista)                  # máximo
min(lista)                  # mínimo
abs(-5)                     # valor absoluto
round(3.7)                  # redondeo

# I/O
print("texto")
input("mensaje: ")          # devuelve string
```

---

## 🎯 Comprensiones

```python
# Lista
[x**2 for x in range(5)]
[x for x in nums if x % 2 == 0]

# Diccionario
{x: x**2 for x in range(5)}

# Set
{x**2 for x in range(-5, 6)}

# Generador (lazy)
(x**2 for x in range(1000000))
```

---

## 🚨 Manejo de errores

```python
try:
    # código que puede fallar
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    # se ejecuta si no hubo error
    print("Todo bien")
finally:
    # siempre se ejecuta
    print("Limpieza")
```

---

## 🧪 Debugging

```python
# Imprimir
print(f"Valor: {variable}")
print(f"Tipo: {type(variable)}")

# Assert
assert edad >= 0, "Edad no puede ser negativa"

# Breakpoint (Python 3.7+)
breakpoint()
```

---

## 💡 Convenciones y buenas prácticas

```python
# Nombres
variable_nombre          # snake_case para variables y funciones
CONSTANTE               # MAYÚSCULAS para constantes
ClaseNombre             # PascalCase para clases

# Espacios
# ✅ Sí:
x = 1
y = 2
if x == 1:
    pass

# ❌ No:
x=1
y = 2
if x==1:
    pass

# Imports
# Orden: stdlib → terceros → locales
import os
import sys

import numpy
import pandas

from mi_modulo import funcion

# Documentación
def funcion(param):
    """
    Breve descripción.
    
    Args:
        param: descripción
    
    Returns:
        descripción del valor devuelto
    """
    pass
```

---

## 🎨 Patrones comunes

```python
# Swap de variables
a, b = b, a

# Múltiples comparaciones
if x < y < z:
    pass

# Default dict
from collections import defaultdict
d = defaultdict(list)
d["key"].append(1)  # no error si key no existe

# Ternario anidado
resultado = (
    "caso1" if cond1 else
    "caso2" if cond2 else
    "caso3"
)

# Enumerate con índice custom
for i, elem in enumerate(lista, start=1):
    print(f"{i}. {elem}")

# Zip para combinar
nombres = ["Ana", "Juan"]
edades = [25, 30]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre}: {edad}")

# Any y All
any([False, False, True])   # True
all([True, True, False])    # False
```

---

## 🦭 Operador Morsa (`:=`) - Python 3.8+

```python
# Asignación en expresiones
# Sintaxis: (variable := valor)

# ❌ Sin operador morsa
nombre = input("Nombre: ")
if nombre != "":
    print(f"Hola, {nombre}")

# ✅ Con operador morsa
if (nombre := input("Nombre: ")) != "":
    print(f"Hola, {nombre}")

# Bucle while con input
while (comando := input("Comando: ")) != "salir":
    print(f"Ejecutando: {comando}")

# En list comprehensions
numeros = [1, 2, 3, 4, 5]
cuadrados_pares = [c for n in numeros if (c := n**2) % 2 == 0]
# Resultado: [4, 16]

# Validación con lectura de archivo
with open("datos.txt") as f:
    while (linea := f.readline()):
        print(linea.strip())

# ⚠️ Recuerda: Solo úsalo cuando mejore la legibilidad
# Ver cheatsheets/07_operador_morsa.md para guía completa
```

---

## 📚 Recursos

- [Documentación oficial](https://docs.python.org/es/3/)
- [PEP 8 - Guía de estilo](https://pep8.org/)
- [Python Tutor - Visualizador](http://pythontutor.com/)
- [Real Python - Tutoriales](https://realpython.com/)

---

**💡 Tip**: Imprime esta página y tenla cerca mientras programas. ¡Practica cada día para dominar Python!
