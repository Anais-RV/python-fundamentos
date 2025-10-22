# 📘 Cheat Sheet: Estructuras de datos básicas

## 🎯 Conceptos clave

Python tiene varios tipos de datos incorporados para trabajar con información de diferentes formas.

---

## 🔤 Cadenas de texto (str)

### Crear y manipular strings

```python
# Definición
nombre = "Python"
mensaje = 'Hola mundo'
multilinea = """Este texto
ocupa varias líneas"""

# Concatenación
saludo = "Hola" + " " + "mundo"  # "Hola mundo"
repeticion = "Ja" * 3  # "JaJaJa"

# Acceso por índice (comienza en 0)
palabra = "Python"
palabra[0]   # 'P'
palabra[-1]  # 'n' (último carácter)
palabra[2:5] # 'tho' (slicing)
```

### Métodos comunes de strings

```python
texto = "Hola Mundo"

texto.lower()        # "hola mundo"
texto.upper()        # "HOLA MUNDO"
texto.capitalize()   # "Hola mundo"
texto.title()        # "Hola Mundo"

texto.replace("Mundo", "Python")  # "Hola Python"
texto.split()        # ['Hola', 'Mundo']
" ".join(['a', 'b'])  # "a b"

texto.startswith("Hola")  # True
texto.endswith("o")       # False
texto.find("Mundo")       # 5 (índice donde empieza)

len(texto)  # 10 (longitud)
```

### f-strings (formato moderno) ⭐

Las **f-strings** (formatted string literals) son la forma moderna y recomendada de formatear strings en Python (desde Python 3.6).

#### ¿Por qué son importantes?

✅ **Legibles**: el código es claro y fácil de entender  
✅ **Rápidas**: más eficientes que `.format()` o concatenación  
✅ **Potentes**: permiten expresiones Python dentro de `{}`  
✅ **Profesionales**: son el estándar actual en la industria

#### Sintaxis básica

```python
nombre = "Ana"
edad = 25

# f-string básica
mensaje = f"Me llamo {nombre} y tengo {edad} años"
print(mensaje)  # Me llamo Ana y tengo 25 años

# Con expresiones directas
print(f"El doble de {edad} es {edad * 2}")  # El doble de 25 es 50

# Con métodos
print(f"Hola, {nombre.upper()}")  # Hola, ANA
```

#### Formato de números

```python
precio = 19.99

# Dos decimales
print(f"Total: {precio:.2f}€")  # Total: 19.99€

# Separadores de miles
print(f"Población: {1234567:,}")  # Población: 1,234,567

# Porcentajes
tasa = 0.856
print(f"Aprobados: {tasa:.1%}")  # Aprobados: 85.6%

# Alinear texto
nombre = "Ana"
print(f"|{nombre:>10}|")  # |       Ana| (alineado derecha)
print(f"|{nombre:<10}|")  # |Ana       | (alineado izquierda)
print(f"|{nombre:^10}|")  # |   Ana    | (centrado)
```

#### Alternativas antiguas (evitar)

```python
# ❌ Concatenación (poco legible)
mensaje = "Me llamo " + nombre + " y tengo " + str(edad) + " años"

# ❌ .format() (más verboso)
mensaje = "Me llamo {} y tengo {} años".format(nombre, edad)

# ✅ f-strings (moderno y limpio)
mensaje = f"Me llamo {nombre} y tengo {edad} años"
```

---

## 🔢 Números (int y float)

### Operadores aritméticos

```python
suma = 10 + 5         # 15
resta = 10 - 5        # 5
multiplicacion = 3 * 4  # 12
division = 10 / 3     # 3.333... (float)
division_entera = 10 // 3  # 3 (int)
modulo = 10 % 3       # 1 (resto)
potencia = 2 ** 3     # 8
```

### Funciones útiles con números

```python
abs(-5)        # 5 (valor absoluto)
round(3.7)     # 4 (redondeo)
round(3.14159, 2)  # 3.14 (redondeo a 2 decimales)

max(5, 10, 3)  # 10
min(5, 10, 3)  # 3
sum([1, 2, 3]) # 6
```

### Conversiones

```python
int(3.9)       # 3 (trunca decimales)
float(5)       # 5.0
int("42")      # 42
float("3.14")  # 3.14
str(100)       # "100"
```

---

## ✅ Booleanos (bool)

```python
es_mayor = True
esta_activo = False

# Operadores lógicos
True and False   # False
True or False    # True
not True         # False

# Comparaciones devuelven booleanos
5 > 3    # True
10 == 10 # True
7 != 7   # False
```

### Valores considerados `False`

```python
bool(0)       # False
bool("")      # False
bool(None)    # False
bool([])      # False (lista vacía)
bool({})      # False (diccionario vacío)

# Cualquier otro valor es True
bool(1)       # True
bool("hola")  # True
bool([1, 2])  # True
```

---

## 🔄 Conversiones de tipo (casting)

```python
# String a número
edad = int("25")           # 25
precio = float("19.99")    # 19.99

# Número a string
texto = str(42)            # "42"

# A booleano
bool(1)        # True
bool(0)        # False
bool("texto")  # True

# Casos especiales
int(3.9)       # 3 (trunca, no redondea)
int("3.9")     # ❌ ValueError
int(float("3.9"))  # ✅ 3
```

---

## 🧮 Operadores de comparación

```python
5 == 5    # True (igual que)
5 != 3    # True (distinto de)
5 > 3     # True (mayor que)
5 < 10    # True (menor que)
5 >= 5    # True (mayor o igual)
3 <= 2    # False (menor o igual)
```

---

## 🔗 Operadores lógicos

```python
# AND: ambos deben ser True
True and True    # True
True and False   # False

# OR: al menos uno debe ser True
True or False    # True
False or False   # False

# NOT: invierte el valor
not True         # False
not False        # True

# Combinados
edad = 25
es_adulto = edad >= 18 and edad < 65
```

---

## 🎨 Ejemplos prácticos

### Validación de entrada con tipos

```python
# Validación de entrada
nombre = input("Nombre: ")
edad_str = input("Edad: ")

# Conversión y validación
if edad_str.isdigit():
    edad = int(edad_str)
    
    if edad >= 18:
        print(f"{nombre.title()}, eres mayor de edad")
    else:
        años_faltan = 18 - edad
        print(f"Te faltan {años_faltan} años para ser mayor de edad")
else:
    print("Por favor, introduce un número válido")
```

---

## 🚨 Errores comunes

❌ **Concatenar string con número**
```python
"Tengo " + 25 + " años"  # TypeError
```
✅ Solución: `"Tengo " + str(25) + " años"` o usar f-string

❌ **División por cero**
```python
10 / 0  # ZeroDivisionError
```
✅ Solución: verificar antes con `if divisor != 0:`

❌ **Comparar tipos diferentes**
```python
"10" == 10  # False (son tipos diferentes)
```
✅ Solución: convertir primero `int("10") == 10  # True`

❌ **Confundir `=` con `==`**
```python
if edad = 18:  # SyntaxError
```
✅ Solución: `if edad == 18:`

---

## 📌 Conceptos clave

- Los **strings** son inmutables (no se pueden modificar en su lugar)
- La **división** `/` siempre devuelve float, usa `//` para división entera
- Los **booleanos** son subclase de int: `True == 1` y `False == 0`
- Usa **f-strings** para formatear cadenas de forma legible
