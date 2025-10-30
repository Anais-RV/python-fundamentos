# EJERCICIO AUTÓNOMO 1: BOOLEANS
# Enunciado: evalúa condiciones simples (>=, ==) y muestra True/False.

# Variables de dos números enteros que piden al usuario
num1 = input("Escribe un número: ")
num2 = input("Escribe otro número: ")

num1 = int(num1)
num2 = int(num2)

# Declaramos variables de las condiciones simples:
# Condición si el primer número es Mayor o igual que el segundo número
mayorigualque = num1 >= num2
# Condición si el primer número es Menor o igual que el segundo número
menorigualque = num1 <= num2
# Condición si el primer número es Igual que el segundo número
igualque = num1 == num2
# Condición si el primer número es Distinto que el segundo número
distintoque = num1 != num2
# Condición si el primer número es Mayor que el segundo número
mayorque = num1 > num2
# Condición si el primer número es Menor que el segundo número
menorque = num1 < num2

# Imprimir las condiciones simples en consola
print(f"CONDICIONES SIMPLES:")
print(f"{num1} >= {num2} : {num1 + num2}")
print(f"{num1} <= {num2} : {menorigualque}")
print(f"{num1} == {num2} : {igualque}")
print(f"{num1} != {num2} : {distintoque}")
print(f"{num1} > {num2} : {mayorque}")
print(f"{num1} < {num2} : {menorque}")

# Primer test: introducir '4' como num1 y '6' como num2. 
# Resultado:
# CONDICIONES SIMPLES:
# 4 >= 6 : False
# 4 <= 6 : True
# 4 == 6 : False
# 4 != 6 : True
# 4 > 6 : False
# 4 < 6 : True