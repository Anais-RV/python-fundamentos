# 📘 Cheat Sheet: Funciones

## 🎯 Conceptos clave

Las funciones son bloques de código reutilizables que realizan una tarea específica. Ayudan a organizar el código, evitar repetición y hacerlo más legible.

---

## 📦 Definir y llamar funciones

### Sintaxis básica

```python
def nombre_funcion():
    """Docstring: describe qué hace la función"""
    # código de la función
    pass

# Llamar a la función
nombre_funcion()
```

### Ejemplo simple

```python
def saludar():
    """Imprime un saludo"""
    print("¡Hola, mundo!")

saludar()  # ¡Hola, mundo!
```

---

## 📥 Parámetros y argumentos

### Parámetros posicionales

```python
def saludar(nombre):
    """Saluda a una persona por su nombre"""
    print(f"¡Hola, {nombre}!")

saludar("Ana")  # ¡Hola, Ana!

# Varios parámetros
def sumar(a, b):
    """Suma dos números"""
    resultado = a + b
    print(f"{a} + {b} = {resultado}")

sumar(5, 3)  # 5 + 3 = 8
```

### Parámetros con valores por defecto

```python
def saludar(nombre, idioma="español"):
    """Saluda en diferentes idiomas"""
    if idioma == "español":
        print(f"¡Hola, {nombre}!")
    elif idioma == "inglés":
        print(f"Hello, {nombre}!")

saludar("Ana")              # ¡Hola, Ana!
saludar("John", "inglés")   # Hello, John!
```

### Argumentos con nombre (keyword arguments)

```python
def crear_perfil(nombre, edad, ciudad):
    print(f"{nombre}, {edad} años, vive en {ciudad}")

# Orden diferente usando nombres
crear_perfil(edad=25, ciudad="Madrid", nombre="Ana")
```

### Número variable de argumentos

```python
# *args: número variable de argumentos posicionales (tupla)
def sumar_todos(*numeros):
    """Suma cualquier cantidad de números"""
    total = sum(numeros)
    return total

print(sumar_todos(1, 2, 3))        # 6
print(sumar_todos(10, 20, 30, 40)) # 100

# **kwargs: número variable de argumentos con nombre (diccionario)
def mostrar_info(**datos):
    """Muestra información en forma de clave: valor"""
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=25, ciudad="Madrid")
# nombre: Ana
# edad: 25
# ciudad: Madrid
```

---

## 🔙 Return: devolver valores

### Return simple

```python
def sumar(a, b):
    """Devuelve la suma de dos números"""
    return a + b

resultado = sumar(5, 3)
print(resultado)  # 8
```

### Return múltiple

```python
def operaciones(a, b):
    """Devuelve varias operaciones a la vez"""
    suma = a + b
    resta = a - b
    producto = a * b
    return suma, resta, producto

s, r, p = operaciones(10, 5)
print(s, r, p)  # 15 5 50
```

### Return condicional

```python
def es_par(numero):
    """Devuelve True si el número es par"""
    if numero % 2 == 0:
        return True
    else:
        return False

# Versión simplificada
def es_par(numero):
    return numero % 2 == 0

print(es_par(4))  # True
print(es_par(7))  # False
```

### Return sin valor (None)

```python
def saludar(nombre):
    print(f"Hola, {nombre}")
    # return implícito de None

resultado = saludar("Ana")  # Hola, Ana
print(resultado)  # None
```

---

## 🌍 Scope: ámbito de variables

### Variables locales vs globales

```python
# Variable global
contador = 0

def incrementar():
    # Variable local
    contador = 10  # Esta es diferente de la global
    print(f"Dentro: {contador}")

incrementar()  # Dentro: 10
print(f"Fuera: {contador}")  # Fuera: 0
```

### Modificar variable global

```python
contador = 0

def incrementar():
    global contador  # Indica que usamos la variable global
    contador += 1

incrementar()
print(contador)  # 1
```

### Variables no locales (nested functions)

```python
def exterior():
    x = 10
    
    def interior():
        nonlocal x  # Modifica la variable de la función exterior
        x += 5
    
    interior()
    print(x)  # 15

exterior()
```

---

## 🎭 Funciones lambda

### Sintaxis

```python
# Función normal
def cuadrado(x):
    return x ** 2

# Equivalente con lambda
cuadrado = lambda x: x ** 2

print(cuadrado(5))  # 25
```

### Uso común: con funciones de orden superior

```python
# Ordenar por longitud
palabras = ["python", "es", "genial"]
ordenadas = sorted(palabras, key=lambda x: len(x))
print(ordenadas)  # ['es', 'python', 'genial']

# Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6]

# Mapear: elevar al cuadrado
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25, 36]
```

---

## 📚 Docstrings

### Documentar funciones

```python
def calcular_area(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Args:
        base (float): La base del rectángulo
        altura (float): La altura del rectángulo
    
    Returns:
        float: El área del rectángulo
    
    Example:
        >>> calcular_area(5, 3)
        15
    """
    return base * altura

# Acceder al docstring
print(calcular_area.__doc__)
help(calcular_area)
```

---

## 🎨 Ejemplos prácticos

### Calculadora simple

```python
def calculadora(a, b, operacion):
    """Realiza operaciones matemáticas básicas"""
    if operacion == "+":
        return a + b
    elif operacion == "-":
        return a - b
    elif operacion == "*":
        return a * b
    elif operacion == "/":
        if b != 0:
            return a / b
        else:
            return "Error: división por cero"
    else:
        return "Operación no válida"

print(calculadora(10, 5, "+"))   # 15
print(calculadora(10, 5, "*"))   # 50
```

### Validación de entrada

```python
def obtener_numero_positivo(mensaje):
    """Solicita al usuario un número positivo válido"""
    while True:
        try:
            numero = float(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("El número debe ser positivo")
        except ValueError:
            print("Por favor, introduce un número válido")

edad = obtener_numero_positivo("Introduce tu edad: ")
print(f"Tienes {edad} años")
```

### Contador de vocales

```python
def contar_vocales(texto):
    """Cuenta las vocales en un texto"""
    vocales = "aeiouAEIOU"
    contador = 0
    
    for letra in texto:
        if letra in vocales:
            contador += 1
    
    return contador

frase = "Python es genial"
print(f"Vocales: {contar_vocales(frase)}")  # Vocales: 5
```

### Generador de saludos

```python
def saludar_multiple(*nombres, formal=False):
    """Saluda a varias personas de forma formal o informal"""
    saludos = []
    
    for nombre in nombres:
        if formal:
            saludo = f"Estimado/a {nombre}"
        else:
            saludo = f"¡Hola, {nombre}!"
        saludos.append(saludo)
    
    return saludos

print(saludar_multiple("Ana", "Juan", "María"))
# ['¡Hola, Ana!', '¡Hola, Juan!', '¡Hola, María!']

print(saludar_multiple("Ana", "Juan", formal=True))
# ['Estimado/a Ana', 'Estimado/a Juan']
```

---

## 🚨 Errores comunes

❌ **Olvidar el return**
```python
def sumar(a, b):
    a + b  # No devuelve nada

resultado = sumar(3, 5)
print(resultado)  # None
```
✅ Solución: `return a + b`

❌ **Modificar variable global sin declararlo**
```python
x = 10

def cambiar():
    x = 20  # Crea una variable local

cambiar()
print(x)  # 10 (no cambió)
```
✅ Solución: usar `global x` dentro de la función

❌ **Parámetros mutables por defecto**
```python
def agregar(elemento, lista=[]):
    lista.append(elemento)
    return lista

print(agregar(1))  # [1]
print(agregar(2))  # [1, 2] ← ¡La lista persiste!
```
✅ Solución: usar `None` como valor por defecto
```python
def agregar(elemento, lista=None):
    if lista is None:
        lista = []
    lista.append(elemento)
    return lista
```

❌ **Confundir print con return**
```python
def sumar(a, b):
    print(a + b)  # Solo imprime, no devuelve

resultado = sumar(3, 5) * 2  # TypeError
```
✅ Solución: usar `return a + b`

---

## 📌 Conceptos clave

- Las funciones deben hacer **una sola cosa** y hacerla bien
- Usa nombres descriptivos: `calcular_total()` mejor que `calc()`
- Prefiere `return` sobre `print` para reutilización
- Documenta con **docstrings** las funciones complejas
- Los parámetros por defecto se evalúan **una sola vez** al definir la función
- `*args` captura argumentos posicionales extra como tupla
- `**kwargs` captura argumentos con nombre extra como diccionario
- Las variables dentro de una función son **locales** por defecto
