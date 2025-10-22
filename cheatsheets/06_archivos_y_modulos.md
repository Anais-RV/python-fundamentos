# 📘 Cheat Sheet: Archivos y Módulos

## 🎯 Conceptos clave

Python permite leer y escribir archivos para persistir datos, y organizar código en módulos reutilizables.

---

## 📂 Manejo de archivos

### Abrir y cerrar archivos

```python
# Forma básica (requiere cerrar manualmente)
archivo = open("datos.txt", "r")
contenido = archivo.read()
archivo.close()

# Forma recomendada (with cierra automáticamente)
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
# El archivo se cierra automáticamente al salir del bloque
```

### Modos de apertura

```python
# Lectura
"r"   # lectura (error si no existe)
"rb"  # lectura binaria

# Escritura
"w"   # escritura (crea o sobrescribe)
"wb"  # escritura binaria
"a"   # append (añade al final)

# Lectura y escritura
"r+"  # lectura y escritura
"w+"  # escritura y lectura (sobrescribe)
```

---

## 📖 Lectura de archivos

### Leer todo el contenido

```python
# read(): devuelve todo como string
with open("datos.txt", "r") as f:
    contenido = f.read()
    print(contenido)

# readlines(): devuelve lista de líneas
with open("datos.txt", "r") as f:
    lineas = f.readlines()
    for linea in lineas:
        print(linea.strip())  # strip() elimina \n
```

### Leer línea por línea

```python
# Forma eficiente (no carga todo en memoria)
with open("datos.txt", "r") as f:
    for linea in f:
        print(linea.strip())

# readline(): lee una línea cada vez
with open("datos.txt", "r") as f:
    primera = f.readline()
    segunda = f.readline()
```

### Lectura con encoding

```python
# Especificar codificación (importante para textos en español)
with open("datos.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
```

---

## ✍️ Escritura de archivos

### Escribir texto

```python
# write(): escribe un string
with open("salida.txt", "w") as f:
    f.write("Primera línea\n")
    f.write("Segunda línea\n")

# writelines(): escribe lista de strings
lineas = ["línea 1\n", "línea 2\n", "línea 3\n"]
with open("salida.txt", "w") as f:
    f.writelines(lineas)
```

### Añadir al final (append)

```python
# Modo "a" no sobrescribe
with open("log.txt", "a") as f:
    f.write("Nueva entrada\n")
```

### Escribir con formato

```python
nombre = "Ana"
edad = 25

with open("persona.txt", "w") as f:
    f.write(f"Nombre: {nombre}\n")
    f.write(f"Edad: {edad}\n")

# O usar print con file
with open("persona.txt", "w") as f:
    print(f"Nombre: {nombre}", file=f)
    print(f"Edad: {edad}", file=f)
```

---

## 🗂️ Trabajar con rutas

### Módulo `os.path`

```python
import os

# Verificar si existe
os.path.exists("archivo.txt")  # True/False
os.path.isfile("archivo.txt")  # True si es archivo
os.path.isdir("carpeta")       # True si es directorio

# Información de rutas
os.path.basename("/ruta/archivo.txt")  # "archivo.txt"
os.path.dirname("/ruta/archivo.txt")   # "/ruta"
os.path.splitext("datos.txt")          # ("datos", ".txt")

# Construir rutas
ruta = os.path.join("carpeta", "subcarpeta", "archivo.txt")
# carpeta/subcarpeta/archivo.txt (ajusta separadores por OS)

# Ruta absoluta
os.path.abspath("archivo.txt")
```

### Módulo `pathlib` (moderno)

```python
from pathlib import Path

# Crear objeto Path
ruta = Path("datos.txt")

# Verificar existencia
ruta.exists()       # True/False
ruta.is_file()      # True si es archivo
ruta.is_dir()       # True si es directorio

# Información
ruta.name           # "datos.txt"
ruta.stem           # "datos" (sin extensión)
ruta.suffix         # ".txt"
ruta.parent         # Path de la carpeta padre

# Leer/escribir directamente
contenido = ruta.read_text(encoding="utf-8")
ruta.write_text("Nuevo contenido", encoding="utf-8")

# Construir rutas
carpeta = Path("proyecto")
archivo = carpeta / "datos" / "info.txt"
```

---

## 📦 Módulos y paquetes

### Importar módulos

```python
# Importar módulo completo
import math
print(math.pi)  # 3.141592...

# Importar con alias
import math as m
print(m.sqrt(16))  # 4.0

# Importar elementos específicos
from math import pi, sqrt
print(pi)
print(sqrt(16))

# Importar todo (no recomendado)
from math import *
```

### Crear tu propio módulo

```python
# archivo: operaciones.py
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

PI = 3.14159

# archivo: main.py
import operaciones

resultado = operaciones.sumar(5, 3)
print(operaciones.PI)
```

### Estructura de paquetes

```
mi_paquete/
├── __init__.py         # convierte la carpeta en paquete
├── modulo1.py
├── modulo2.py
└── sub_paquete/
    ├── __init__.py
    └── modulo3.py
```

```python
# Importar desde paquete
from mi_paquete import modulo1
from mi_paquete.sub_paquete import modulo3

# __init__.py puede definir qué se exporta
# __init__.py:
from .modulo1 import funcion1
from .modulo2 import funcion2

# Ahora se puede usar:
from mi_paquete import funcion1, funcion2
```

---

## 🛠️ Módulos útiles de la biblioteca estándar

### `os` - Interacción con el sistema operativo

```python
import os

os.getcwd()                 # directorio actual
os.chdir("/nueva/ruta")     # cambiar directorio
os.listdir(".")             # listar archivos en directorio
os.mkdir("nueva_carpeta")   # crear directorio
os.remove("archivo.txt")    # eliminar archivo
os.rename("viejo.txt", "nuevo.txt")  # renombrar
```

### `sys` - Parámetros y funciones del sistema

```python
import sys

sys.argv        # argumentos de línea de comandos
sys.exit()      # salir del programa
sys.version     # versión de Python
sys.path        # rutas donde Python busca módulos
```

### `json` - Trabajar con JSON

```python
import json

# Diccionario a JSON
datos = {"nombre": "Ana", "edad": 25}
json_str = json.dumps(datos)
# '{"nombre": "Ana", "edad": 25}'

# JSON a diccionario
datos = json.loads(json_str)

# Leer JSON desde archivo
with open("datos.json", "r") as f:
    datos = json.load(f)

# Escribir JSON a archivo
with open("datos.json", "w") as f:
    json.dump(datos, f, indent=2)
```

### `csv` - Archivos CSV

```python
import csv

# Leer CSV
with open("datos.csv", "r") as f:
    lector = csv.reader(f)
    for fila in lector:
        print(fila)  # cada fila es una lista

# Escribir CSV
datos = [
    ["Nombre", "Edad"],
    ["Ana", 25],
    ["Juan", 30]
]

with open("salida.csv", "w", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerows(datos)

# CSV con diccionarios
with open("datos.csv", "r") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        print(fila["Nombre"], fila["Edad"])
```

### `datetime` - Fechas y horas

```python
from datetime import datetime, date, time, timedelta

# Fecha y hora actual
ahora = datetime.now()
hoy = date.today()

# Crear fecha específica
fecha = date(2024, 12, 25)
hora = time(14, 30, 0)

# Formatear
print(ahora.strftime("%d/%m/%Y %H:%M"))  # "25/10/2024 14:30"

# Parsear string
fecha = datetime.strptime("25/12/2024", "%d/%m/%Y")

# Operaciones
mañana = hoy + timedelta(days=1)
hace_una_semana = hoy - timedelta(weeks=1)
```

### `random` - Números aleatorios

```python
import random

random.random()           # float entre 0 y 1
random.randint(1, 10)     # int entre 1 y 10
random.choice([1, 2, 3])  # elemento aleatorio
random.shuffle(lista)     # mezcla la lista in-place

# Ejemplo: lanzar dado
dado = random.randint(1, 6)
```

---

## 🎨 Ejemplos prácticos

### Contador de palabras en archivo

```python
def contar_palabras(archivo):
    """Cuenta palabras en un archivo"""
    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read()
        palabras = contenido.split()
        return len(palabras)

total = contar_palabras("texto.txt")
print(f"Total de palabras: {total}")
```

### Log de eventos

```python
from datetime import datetime

def escribir_log(mensaje):
    """Añade entrada al archivo de log con timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("app.log", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {mensaje}\n")

escribir_log("Aplicación iniciada")
escribir_log("Usuario Ana ha ingresado")
escribir_log("Error en base de datos")
```

### Guardar y cargar configuración

```python
import json

def guardar_config(datos, archivo="config.json"):
    """Guarda configuración en JSON"""
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2)

def cargar_config(archivo="config.json"):
    """Carga configuración desde JSON"""
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Uso
config = {
    "idioma": "español",
    "tema": "oscuro",
    "notificaciones": True
}

guardar_config(config)
config_cargada = cargar_config()
```

### Procesar archivo CSV

```python
import csv

def leer_notas(archivo):
    """Lee notas de estudiantes desde CSV"""
    estudiantes = []
    
    with open(archivo, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        
        for fila in lector:
            estudiante = {
                "nombre": fila["nombre"],
                "nota": float(fila["nota"])
            }
            estudiantes.append(estudiante)
    
    return estudiantes

def calcular_promedio(estudiantes):
    """Calcula promedio de notas"""
    total = sum(e["nota"] for e in estudiantes)
    return total / len(estudiantes)

estudiantes = leer_notas("notas.csv")
promedio = calcular_promedio(estudiantes)
print(f"Promedio del grupo: {promedio:.2f}")
```

---

## 🚨 Errores comunes

❌ **Olvidar cerrar archivo**
```python
f = open("archivo.txt", "r")
contenido = f.read()
# ¡Falta f.close()!
```
✅ Solución: usar `with` (cierra automáticamente)

❌ **Problemas de encoding**
```python
with open("texto_español.txt", "r") as f:
    contenido = f.read()  # UnicodeDecodeError
```
✅ Solución: especificar encoding: `open(..., encoding="utf-8")`

❌ **Ruta relativa incorrecta**
```python
# Si estás en /home/usuario y el script está en /home/usuario/proyecto
open("datos.txt")  # busca en /home/usuario, no en /home/usuario/proyecto
```
✅ Solución: usar ruta absoluta o Path.cwd()

❌ **Sobrescribir sin querer**
```python
with open("importante.txt", "w") as f:
    f.write("nuevo")  # ¡Borra todo el contenido anterior!
```
✅ Para añadir: usar modo `"a"` en lugar de `"w"`

❌ **Importación circular**
```python
# modulo_a.py importa modulo_b.py
# modulo_b.py importa modulo_a.py
# ¡Error de importación circular!
```
✅ Solución: reorganizar código o usar importación local

---

## 📌 Conceptos clave

- Usa **`with open()`** para manejar archivos (cierra automáticamente)
- Especifica **encoding="utf-8"** para textos con acentos/ñ
- **`pathlib.Path`** es más moderno y multiplataforma que `os.path`
- Los módulos se buscan en `sys.path` (incluye directorio actual)
- `__init__.py` convierte una carpeta en paquete importable
- JSON es ideal para guardar estructuras de datos (listas, diccionarios)
- CSV es perfecto para datos tabulares (hojas de cálculo)
- Maneja errores con `try/except` al trabajar con archivos
