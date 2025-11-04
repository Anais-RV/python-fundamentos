# 🦭 Operador Morsa (Walrus Operator) `:=`

> **Python 3.8+** - Asignación en expresiones

El operador morsa (`:=`) permite **asignar y usar una variable en la misma expresión**. Su nombre viene de su parecido visual con un emoji de morsa rotado 🦭.

---

## 🎯 Conceptos clave

- **Sintaxis**: `(variable := expresión)`
- **Propósito**: Reducir código repetitivo y mejorar legibilidad
- **Ámbito**: La variable queda disponible en el scope actual
- **Cuándo usarlo**: Cuando necesitas el valor de una expresión más de una vez

---

## 📖 Sintaxis básica

### Sin operador morsa (tradicional)
```python
# Calcular y luego usar
valor = len(nombre)
if valor > 10:
    print(f"Nombre largo: {valor} caracteres")
```

### Con operador morsa
```python
# Asignar y usar en la misma línea
if (valor := len(nombre)) > 10:
    print(f"Nombre largo: {valor} caracteres")
```

---

## 🎨 Casos de uso prácticos

### 1️⃣ Bucles while con input

**❌ Antes (repetitivo)**
```python
comando = input("Comando: ")
while comando != "salir":
    print(f"Ejecutando: {comando}")
    comando = input("Comando: ")
```

**✅ Con operador morsa**
```python
while (comando := input("Comando: ")) != "salir":
    print(f"Ejecutando: {comando}")
```

### 2️⃣ Validación de datos

**❌ Antes**
```python
edad = input("Edad: ")
try:
    edad_num = int(edad)
    if edad_num >= 18:
        print(f"Acceso permitido: {edad_num} años")
except ValueError:
    print("Edad inválida")
```

**✅ Con operador morsa**
```python
if (edad := input("Edad: ")).isdigit() and (edad_num := int(edad)) >= 18:
    print(f"Acceso permitido: {edad_num} años")
else:
    print("Edad inválida o menor de edad")
```

### 3️⃣ Procesamiento de archivos

**❌ Antes**
```python
archivo = open("datos.txt")
linea = archivo.readline()
while linea:
    print(linea.strip())
    linea = archivo.readline()
archivo.close()
```

**✅ Con operador morsa**
```python
with open("datos.txt") as archivo:
    while (linea := archivo.readline()):
        print(linea.strip())
```

### 4️⃣ List comprehensions con filtrado

**❌ Antes**
```python
# Calcular cuadrados solo si son pares
numeros = [1, 2, 3, 4, 5]
cuadrados_pares = []
for n in numeros:
    cuadrado = n ** 2
    if cuadrado % 2 == 0:
        cuadrados_pares.append(cuadrado)
```

**✅ Con operador morsa**
```python
numeros = [1, 2, 3, 4, 5]
cuadrados_pares = [cuadrado for n in numeros if (cuadrado := n ** 2) % 2 == 0]
# Resultado: [4, 16]
```

### 5️⃣ Regex con captura de grupos

**❌ Antes**
```python
import re

texto = "Usuario: ana123"
match = re.search(r"Usuario: (\w+)", texto)
if match:
    usuario = match.group(1)
    print(f"Encontrado: {usuario}")
```

**✅ Con operador morsa**
```python
import re

texto = "Usuario: ana123"
if (match := re.search(r"Usuario: (\w+)", texto)):
    print(f"Encontrado: {match.group(1)}")
```

### 6️⃣ Cálculos costosos en condicionales

**❌ Antes**
```python
def procesar_datos(datos):
    resultado = analisis_complejo(datos)  # Operación costosa
    if resultado > umbral:
        return resultado * 2
    else:
        return resultado
```

**✅ Con operador morsa**
```python
def procesar_datos(datos):
    if (resultado := analisis_complejo(datos)) > umbral:
        return resultado * 2
    return resultado
```

---

## 🚨 Errores comunes

### ❌ Error 1: Olvidar los paréntesis
```python
# ❌ SyntaxError
if valor := len(nombre) > 10:
    print("largo")

# ✅ Correcto
if (valor := len(nombre)) > 10:
    print("largo")
```

### ❌ Error 2: Usar en lugar de comparación
```python
numeros = [1, 2, 3, 4, 5]

# ❌ Asigna, no compara
if x := 3:  # Siempre True si x no es 0/None/vacío
    print("Esto se ejecuta")

# ✅ Comparación correcta
if (x := obtener_valor()) == 3:
    print("x es 3")
```

### ❌ Error 3: Abusar del operador (código ilegible)
```python
# ❌ Difícil de leer
if (a := func1()) and (b := func2(a)) and (c := func3(b)) > 10:
    print(c)

# ✅ Mejor dividir en pasos
a = func1()
b = func2(a)
c = func3(b)
if c > 10:
    print(c)
```

### ❌ Error 4: Scope inesperado
```python
# ❌ La variable 'x' queda en el scope exterior
if (x := 10) > 5:
    print(x)  # 10

print(x)  # 10 (aún existe)

# ✅ Si no quieres contaminar el scope, usa variable temporal
temp = 10
if temp > 5:
    print(temp)
# temp sigue existiendo, pero es más explícito
```

---

## 🤔 Cuándo NO usar el operador morsa

### ❌ 1. Cuando reduce legibilidad
```python
# ❌ Confuso
resultado = [(x, y) for x in range(10) if (y := x ** 2) < 50]

# ✅ Más claro
resultado = []
for x in range(10):
    y = x ** 2
    if y < 50:
        resultado.append((x, y))
```

### ❌ 2. Cuando la asignación normal es más clara
```python
# ❌ Innecesario
print((nombre := "Ana"))

# ✅ Más claro
nombre = "Ana"
print(nombre)
```

### ❌ 3. En código que debe ser compatible con Python < 3.8
```python
# ❌ No funciona en Python 3.7 o anterior
if (n := len(lista)) > 0:
    print(n)

# ✅ Compatible con versiones antiguas
n = len(lista)
if n > 0:
    print(n)
```

---

## 📌 Reglas de oro

✅ **Usa el operador morsa cuando:**
- Reduces duplicación de código
- Mejoras la legibilidad
- Evitas cálculos repetidos

❌ **No uses el operador morsa cuando:**
- El código se vuelve confuso
- Una asignación simple es más clara
- Necesitas compatibilidad con Python < 3.8

---

## 🎯 Ejercicio rápido

Refactoriza este código usando el operador morsa:

```python
# Antes
nombre = input("Nombre: ")
while nombre != "":
    print(f"Hola, {nombre}")
    nombre = input("Nombre: ")
```

<details>
<summary>Ver solución</summary>

```python
# Después
while (nombre := input("Nombre: ")) != "":
    print(f"Hola, {nombre}")
```
</details>

---

## 📚 Referencias

- [PEP 572 - Assignment Expressions](https://www.python.org/dev/peps/pep-0572/)
- [Real Python - Walrus Operator](https://realpython.com/python-walrus-operator/)

---

**Anaïs Rodríguez Villanueva** - Material pedagógico para formación en Python
