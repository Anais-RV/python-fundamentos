# 📘 Cheat Sheet: Colecciones

## 🎯 Conceptos clave

Python ofrece varias estructuras de datos para almacenar colecciones de elementos: listas, tuplas, diccionarios y sets. Cada una tiene características y usos específicos.

---

## 📋 Listas (list)

Las listas son **mutables** (se pueden modificar), **ordenadas** y permiten **elementos duplicados**.

### Crear listas

```python
# Lista vacía
lista = []
lista = list()

# Con elementos
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "pera", "uva"]
mixta = [1, "hola", 3.14, True]  # Pueden ser de tipos diferentes
```

### Acceso y slicing

```python
frutas = ["manzana", "pera", "uva", "naranja"]

# Acceso por índice (empieza en 0)
frutas[0]     # "manzana"
frutas[-1]    # "naranja" (último elemento)
frutas[-2]    # "uva" (penúltimo)

# Slicing [inicio:fin:paso]
frutas[1:3]   # ["pera", "uva"]
frutas[:2]    # ["manzana", "pera"] (desde el inicio)
frutas[2:]    # ["uva", "naranja"] (hasta el final)
frutas[::2]   # ["manzana", "uva"] (cada 2 elementos)
frutas[::-1]  # ["naranja", "uva", "pera", "manzana"] (invertida)
```

### Modificar listas

```python
frutas = ["manzana", "pera", "uva"]

# Cambiar elemento
frutas[1] = "plátano"  # ["manzana", "plátano", "uva"]

# Añadir elementos
frutas.append("kiwi")           # al final
frutas.insert(1, "fresa")       # en posición específica
frutas.extend(["limón", "melón"])  # varios elementos

# Eliminar elementos
frutas.remove("pera")    # elimina la primera ocurrencia
elemento = frutas.pop()  # elimina y devuelve el último
elemento = frutas.pop(0) # elimina y devuelve el índice 0
del frutas[1]            # elimina por índice
frutas.clear()           # vacía la lista
```

### Métodos útiles

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

len(numeros)          # 8 (longitud)
numeros.count(1)      # 2 (cuántas veces aparece)
numeros.index(4)      # 2 (índice de la primera ocurrencia)

numeros.sort()        # ordena in-place: [1, 1, 2, 3, 4, 5, 6, 9]
numeros.reverse()     # invierte: [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() devuelve nueva lista sin modificar la original
ordenada = sorted(numeros)

# Operaciones
3 in numeros          # True (pertenencia)
numeros + [7, 8]      # concatenación
numeros * 2           # repetición
```

### List comprehension

```python
# Sintaxis: [expresion for elemento in iterable if condicion]

# Crear lista de cuadrados
cuadrados = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

# Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6]
pares = [x for x in numeros if x % 2 == 0]
# [2, 4, 6]

# Transformar strings
palabras = ["hola", "mundo"]
mayusculas = [p.upper() for p in palabras]
# ["HOLA", "MUNDO"]

# Con condicional ternario
valores = [1, -2, 3, -4, 5]
absolutos = [x if x >= 0 else -x for x in valores]
# [1, 2, 3, 4, 5]
```

---

## 🔒 Tuplas (tuple)

Las tuplas son **inmutables** (no se pueden modificar), **ordenadas** y permiten **elementos duplicados**.

### Crear tuplas

```python
# Tupla vacía
tupla = ()
tupla = tuple()

# Con elementos
coordenadas = (10, 20)
datos = (1, "hola", 3.14)

# Tupla de un elemento (necesita coma)
una = (5,)  # tupla
no_tupla = (5)  # int
```

### Operaciones

```python
punto = (3, 5)

# Acceso (igual que listas)
punto[0]   # 3
punto[-1]  # 5

# Desempaquetado
x, y = punto
print(x, y)  # 3 5

# Métodos
punto.count(3)  # 1
punto.index(5)  # 1

# No se pueden modificar
# punto[0] = 10  # TypeError
```

### ¿Cuándo usar tuplas?

```python
# Para datos que no deben cambiar
DIAS_SEMANA = ("lunes", "martes", "miércoles", "jueves", "viernes")

# Como claves de diccionario (listas no pueden)
mapa = {(0, 0): "origen", (10, 20): "destino"}

# Para devolver múltiples valores
def min_max(numeros):
    return min(numeros), max(numeros)

minimo, maximo = min_max([3, 1, 4, 1, 5])
```

---

## 🗂️ Diccionarios (dict)

Los diccionarios almacenan pares **clave:valor**, son **mutables** y **no ordenados** (desde Python 3.7 mantienen orden de inserción).

### Crear diccionarios

```python
# Diccionario vacío
persona = {}
persona = dict()

# Con elementos
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

# Otra forma
persona = dict(nombre="Ana", edad=25, ciudad="Madrid")
```

### Acceso y modificación

```python
persona = {"nombre": "Ana", "edad": 25}

# Acceso
persona["nombre"]           # "Ana"
persona.get("edad")         # 25
persona.get("pais", "N/A")  # "N/A" (valor por defecto si no existe)

# Modificar
persona["edad"] = 26
persona["pais"] = "España"  # añade nueva clave

# Eliminar
del persona["ciudad"]
edad = persona.pop("edad")  # elimina y devuelve el valor
persona.clear()             # vacía el diccionario
```

### Métodos útiles

```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

# Obtener claves, valores o pares
persona.keys()    # dict_keys(['nombre', 'edad', 'ciudad'])
persona.values()  # dict_values(['Ana', 25, 'Madrid'])
persona.items()   # dict_items([('nombre', 'Ana'), ...])

# Verificar existencia
"nombre" in persona  # True
"pais" in persona    # False

# Actualizar con otro diccionario
persona.update({"edad": 26, "profesion": "ingeniera"})

# Obtener con valor por defecto
persona.setdefault("pais", "España")  # añade si no existe
```

### Iterar sobre diccionarios

```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

# Sobre claves (por defecto)
for clave in persona:
    print(clave)

# Sobre valores
for valor in persona.values():
    print(valor)

# Sobre pares clave-valor
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

### Dictionary comprehension

```python
# Sintaxis: {clave: valor for elemento in iterable}

# Cuadrados
cuadrados = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Invertir diccionario
original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: clave for clave, valor in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# Con condición
numeros = {"a": 1, "b": 2, "c": 3, "d": 4}
pares = {k: v for k, v in numeros.items() if v % 2 == 0}
# {'b': 2, 'd': 4}
```

---

## 🎲 Sets (conjuntos)

Los sets son colecciones **no ordenadas** de elementos **únicos** (sin duplicados) y **mutables**.

### Crear sets

```python
# Set vacío (no usar {})
conjunto = set()

# Con elementos
numeros = {1, 2, 3, 4, 5}
letras = set("python")  # {'p', 'y', 't', 'h', 'o', 'n'}

# Elimina duplicados automáticamente
unicos = {1, 2, 2, 3, 3, 3}  # {1, 2, 3}
```

### Operaciones básicas

```python
numeros = {1, 2, 3}

# Añadir
numeros.add(4)        # {1, 2, 3, 4}
numeros.update([5, 6])  # {1, 2, 3, 4, 5, 6}

# Eliminar
numeros.remove(3)     # KeyError si no existe
numeros.discard(10)   # no da error si no existe
elemento = numeros.pop()  # elimina y devuelve uno aleatorio

# Verificar
2 in numeros          # True
len(numeros)          # longitud
```

### Operaciones de conjuntos

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Unión (elementos en a o b o ambos)
a | b              # {1, 2, 3, 4, 5, 6}
a.union(b)

# Intersección (elementos en ambos)
a & b              # {3, 4}
a.intersection(b)

# Diferencia (en a pero no en b)
a - b              # {1, 2}
a.difference(b)

# Diferencia simétrica (en a o b pero no en ambos)
a ^ b              # {1, 2, 5, 6}
a.symmetric_difference(b)

# Subconjunto y superconjunto
{1, 2}.issubset({1, 2, 3})     # True
{1, 2, 3}.issuperset({1, 2})   # True
```

### Set comprehension

```python
# Sintaxis: {expresion for elemento in iterable}

# Cuadrados únicos
cuadrados = {x**2 for x in range(-5, 6)}
# {0, 1, 4, 9, 16, 25}

# Vocales únicas en un texto
texto = "python es genial"
vocales = {c for c in texto if c in "aeiou"}
# {'e', 'i', 'a'}
```

---

## 🔄 Conversiones entre colecciones

```python
# Lista a tupla
lista = [1, 2, 3]
tupla = tuple(lista)

# Tupla a lista
lista = list(tupla)

# Lista a set (elimina duplicados)
lista = [1, 2, 2, 3, 3, 3]
conjunto = set(lista)  # {1, 2, 3}

# Set a lista
lista = list(conjunto)

# String a lista
letras = list("python")  # ['p', 'y', 't', 'h', 'o', 'n']

# Lista a string
lista = ['H', 'o', 'l', 'a']
texto = ''.join(lista)  # "Hola"

# Diccionario a lista de claves/valores
d = {"a": 1, "b": 2}
claves = list(d.keys())    # ['a', 'b']
valores = list(d.values()) # [1, 2]
```

---

## 🎨 Ejemplos prácticos

### Contador de palabras

```python
texto = "python es genial python es poderoso"
palabras = texto.split()

contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

print(contador)
# {'python': 2, 'es': 2, 'genial': 1, 'poderoso': 1}

# Con setdefault
contador = {}
for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1
```

### Eliminar duplicados manteniendo orden

```python
def eliminar_duplicados(lista):
    """Elimina duplicados manteniendo el orden"""
    vistos = set()
    resultado = []
    
    for elemento in lista:
        if elemento not in vistos:
            vistos.add(elemento)
            resultado.append(elemento)
    
    return resultado

numeros = [1, 2, 2, 3, 1, 4, 3, 5]
print(eliminar_duplicados(numeros))  # [1, 2, 3, 4, 5]
```

### Agrupar elementos

```python
# Agrupar palabras por longitud
palabras = ["sol", "casa", "rio", "montaña", "luz", "cielo"]

por_longitud = {}
for palabra in palabras:
    longitud = len(palabra)
    if longitud not in por_longitud:
        por_longitud[longitud] = []
    por_longitud[longitud].append(palabra)

print(por_longitud)
# {3: ['sol', 'rio', 'luz'], 4: ['casa'], 7: ['montaña'], 5: ['cielo']}
```

---

## 🚨 Errores comunes

❌ **Modificar lista mientras se itera**
```python
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    if num % 2 == 0:
        numeros.remove(num)  # Comportamiento inesperado
```
✅ Solución: iterar sobre una copia o usar comprensión
```python
numeros = [x for x in numeros if x % 2 != 0]
```

❌ **Usar lista como clave de diccionario**
```python
d = {[1, 2]: "valor"}  # TypeError: unhashable type: 'list'
```
✅ Solución: usar tupla `d = {(1, 2): "valor"}`

❌ **Confundir append y extend**
```python
lista = [1, 2]
lista.append([3, 4])  # [1, 2, [3, 4]]
```
✅ Para añadir elementos individuales: `lista.extend([3, 4])  # [1, 2, 3, 4]`

❌ **Crear set vacío con {}**
```python
vacio = {}  # Esto es un dict, no un set
```
✅ Solución: `vacio = set()`

---

## 📊 Comparación rápida

| Característica | Lista | Tupla | Diccionario | Set |
|---|---|---|---|---|
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Ordenada | ✅ | ✅ | ✅* | ❌ |
| Indexable | ✅ | ✅ | ❌ | ❌ |
| Duplicados | ✅ | ✅ | Keys: ❌ | ❌ |
| Sintaxis | `[]` | `()` | `{}` | `{}` / `set()` |

*Desde Python 3.7 mantienen orden de inserción

---

## 📌 Conceptos clave

- Usa **listas** para colecciones ordenadas que cambiarán
- Usa **tuplas** para datos inmutables o como claves de diccionario
- Usa **diccionarios** para asociar claves con valores (búsqueda rápida)
- Usa **sets** para colecciones únicas y operaciones de conjuntos
- Las **comprensiones** son más rápidas y pythonicas que bucles
- Los diccionarios y sets usan **hash tables** (búsqueda O(1))
