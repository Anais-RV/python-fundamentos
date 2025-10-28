# 1. `es_par(n)` -> bool

def es_par(n):
    return n % 2 == 0

# 2. `area_rectangulo(a, b)`

def area_rectangulo(a,b):
    return a * b

# 3. `formatear_gato(nombre, edad)` -> string con f-string

def formatear_gato(nombre, edad):
    return f"El michi se llama {nombre} y tiene {edad} años."

# 4. `promedio(nums)` con manejo de lista vacía

def promedio(nums):
    if not nums:
        return None
    return sum(nums) / len(nums)

# 5. `leer_edad()` pide una edad por `input()`, valida `ValueError` y retorna un entero o `None`.

def leer_edad():
    try:
        edad = int(imput("¿Cuál es tu edad?: "))
        return edad
    except ValueError:
        return None