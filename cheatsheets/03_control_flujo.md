# 📘 Cheat Sheet: Control de flujo

## 🎯 Conceptos clave

El control de flujo permite que tu programa tome decisiones y repita acciones según condiciones específicas.

---

## 🔀 Condicionales: if, elif, else

### Sintaxis básica

```python
if condicion:
    # código si condicion es True
    pass

if condicion:
    # código si True
else:
    # código si False

if condicion1:
    # código si condicion1 es True
elif condicion2:
    # código si condicion2 es True
else:
    # código si ninguna anterior es True
```

### Ejemplos

```python
edad = 20

if edad >= 18:
    print("Eres mayor de edad")

# Con else
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

# Con elif
if edad < 13:
    print("Niño")
elif edad < 18:
    print("Adolescente")
elif edad < 65:
    print("Adulto")
else:
    print("Adulto mayor")
```

### Condicionales anidados

```python
edad = 25
tiene_licencia = True

if edad >= 18:
    if tiene_licencia:
        print("Puedes conducir")
    else:
        print("Necesitas licencia")
else:
    print("Eres menor de edad")
```

### Operador ternario (inline if)

```python
# Sintaxis: valor_si_true if condicion else valor_si_false
edad = 20
estado = "mayor" if edad >= 18 else "menor"
print(estado)  # "mayor"
```

---

## 🔁 Bucle for

### Iterar sobre rangos

```python
# range(stop): de 0 hasta stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop): de start hasta stop-1
for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

# range(start, stop, step): con saltos
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Descendente
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1
```

### Iterar sobre secuencias

```python
# Sobre strings
for letra in "Python":
    print(letra)  # P, y, t, h, o, n

# Sobre listas
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)

# Con índice usando enumerate
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")
# 0: manzana
# 1: pera
# 2: uva
```

---

## 🔄 Bucle while

### Sintaxis básica

```python
while condicion:
    # código que se repite mientras condicion sea True
    pass
```

### Ejemplos

```python
# Contador simple
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Importante: actualizar la variable

# Validación de entrada
numero = -1
while numero < 0:
    numero = int(input("Introduce un número positivo: "))
```

### Bucle infinito (usar con cuidado)

```python
while True:
    respuesta = input("¿Continuar? (s/n): ")
    if respuesta == "n":
        break  # Sale del bucle
```

---

## 🛑 Control de bucles: break y continue

### `break`: sale del bucle completamente

```python
for i in range(10):
    if i == 5:
        break  # Sale del bucle cuando i es 5
    print(i)  # 0, 1, 2, 3, 4

# Buscar elemento
numeros = [1, 3, 5, 7, 9]
objetivo = 5
encontrado = False

for num in numeros:
    if num == objetivo:
        encontrado = True
        break

if encontrado:
    print(f"Se encontró {objetivo}")
```

### `continue`: salta a la siguiente iteración

```python
for i in range(10):
    if i % 2 == 0:  # Si es par
        continue  # Salta al siguiente i
    print(i)  # Solo imprime impares: 1, 3, 5, 7, 9

# Filtrar elementos
nombres = ["Ana", "", "Juan", "", "María"]
for nombre in nombres:
    if nombre == "":
        continue
    print(f"Hola, {nombre}")
```

---

## 🎯 Bucle for-else y while-else

```python
# for-else: el else se ejecuta si el bucle termina normalmente
for i in range(5):
    if i == 10:
        break
else:
    print("Bucle completado sin break")  # Se ejecuta

# Ejemplo práctico: buscar número primo
numero = 17
for i in range(2, numero):
    if numero % i == 0:
        print(f"{numero} no es primo")
        break
else:
    print(f"{numero} es primo")
```

---

## 🧮 Operadores útiles en condiciones

### Operadores de comparación

```python
a == b  # igual
a != b  # diferente
a > b   # mayor
a < b   # menor
a >= b  # mayor o igual
a <= b  # menor o igual
```

### Operadores lógicos

```python
# AND: ambos deben ser True
edad = 25
if edad >= 18 and edad < 65:
    print("Adulto en edad laboral")

# OR: al menos uno debe ser True
if dia == "sabado" or dia == "domingo":
    print("Es fin de semana")

# NOT: invierte el valor
if not esta_ocupado:
    print("Disponible")
```

### Operadores de pertenencia

```python
# in: verifica si un valor está en una secuencia
if "a" in "palabra":
    print("Contiene 'a'")

vocales = ['a', 'e', 'i', 'o', 'u']
if letra in vocales:
    print("Es una vocal")

# not in
if numero not in [1, 2, 3]:
    print("Número no válido")
```

---

## 🎨 Ejemplos prácticos

### Validación de entrada

```python
while True:
    edad = input("Introduce tu edad: ")
    
    if edad.isdigit():
        edad = int(edad)
        if 0 < edad < 120:
            break
        else:
            print("Edad no válida")
    else:
        print("Por favor, introduce un número")

print(f"Tu edad es {edad}")
```

### Tabla de multiplicar

```python
numero = int(input("¿Qué tabla quieres? "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
```

### Juego de adivinanza

```python
numero_secreto = 42
intentos = 0

while True:
    intento = int(input("Adivina el número: "))
    intentos += 1
    
    if intento == numero_secreto:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos")
        break
    elif intento < numero_secreto:
        print("Demasiado bajo")
    else:
        print("Demasiado alto")
```

---

## 🚨 Errores comunes

❌ **Olvidar los dos puntos**
```python
if edad >= 18  # SyntaxError
    print("Mayor")
```
✅ Solución: `if edad >= 18:`

❌ **Indentación incorrecta**
```python
if edad >= 18:
print("Mayor")  # IndentationError
```
✅ Solución: usar 4 espacios de indentación

❌ **Bucle infinito sin break**
```python
while True:
    print("Esto nunca termina...")
```
✅ Solución: añadir condición de salida con `break`

❌ **Usar = en lugar de ==**
```python
if edad = 18:  # SyntaxError
```
✅ Solución: `if edad == 18:`

❌ **No actualizar variable en while**
```python
i = 0
while i < 5:
    print(i)  # Bucle infinito
```
✅ Solución: `i += 1` dentro del bucle

---

## 📌 Conceptos clave

- La **indentación** (4 espacios) es obligatoria en Python
- `elif` es más eficiente que múltiples `if` independientes
- Usa `for` cuando sepas cuántas iteraciones necesitas
- Usa `while` cuando la condición de parada dependa de algo dinámico
- `break` sale del bucle, `continue` salta a la siguiente iteración
- El bloque `else` en bucles se ejecuta si no hubo `break`
