# EJERCICIO AUTÓNOMO 1: BOOLEANS
# Enunciado: evalúa condiciones simples (>=, ==) y muestra True/False.

# Variables de dos números enteros que piden al usuario
num1 = input("Escribe un número: ")
num2 = input("Escribe otro número: ")

try :

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
    print(f"{num1} >= {num2} : {mayorigualque}")
    print(f"{num1} <= {num2} : {menorigualque}")
    print(f"{num1} == {num2} : {igualque}")
    print(f"{num1} != {num2} : {distintoque}")
    print(f"{num1} > {num2} : {mayorque}")
    print(f"{num1} < {num2} : {menorque}")

except ValueError:
    print("Inválido. Inténtelo de nuevo.")

# Cuarto test: introducir '10' como num1 y '5' como num2. 
# Resultado:
# 10 >= 5 : True
# 10 <= 5 : False
# 10 == 5 : False
# 10 != 5 : True
# 10 > 5 : True
# 10 < 5 : False
# Éxito ✅