# EJERCICIO GUIADO 1: OPREACIONES NUMÉRICAS
# Paso 1: Crea `operaciones.py` y define `a=10`, `b=3`.
# Paso 2: Calcula suma, resta, multiplicación y división.
# Paso 3: Imprime los resultados con f-strings.
# Paso 4: Redondea la división a 2 decimales.


a = 10
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

division = round(division, 2)

print(f"Valor de a: {a}")
print(f"Valor de b: {b}")
print("---------------------------")
print(f"Suma: {a} + {b} = {suma}")
print(f"Resta: {a} - {b} = {resta}")
print(f"Multiplicación: {a} X {b} = {multiplicacion}")
print(f"División: {a} / {b} = {division}")

# Resultado esperado (ptyhon operaciones.py):
# Valor de a: 10
# Valor de b: 3
# ---------------------------
# Suma: 10 + 3 = 13
# Resta: 10 - 3 = 7
# Multiplicación: 10 X 3 = 30
# División: 10 / 3 = 3.33
# Test superado con éxito ✅