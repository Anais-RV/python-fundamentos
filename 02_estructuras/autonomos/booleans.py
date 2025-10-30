# EJERCICIO AUTÓNOMO 1: BOOLEANS
# Enunciado: evalúa condiciones simples (>=, ==) y muestra True/False.

# Variables de dos números enteros
num1 = 4
num2 = 6

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
print(f"{num1} >= {num2} : {mayorigualque}")
print(f"{num1} <= {num2} : {menorigualque}")
print(f"{num1} == {num2} : {igualque}")
print(f"{num1} != {num2} : {distintoque}")
print(f"{num1} > {num2} : {mayorque}")
print(f"{num1} < {num2} : {menorque}")

# RESULTADO ESPERADO con comando 'python booleans.py':
# CONDICIONES SIMPLES:
# 4 >= 6 : False
# 4 <= 6 : True
# 4 == 6 : False
# 4 != 6 : True
# 4 > 6 : False
# 4 < 6 : True