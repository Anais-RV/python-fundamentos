"""
Calculadora v2 - Cuatro operaciones básicas
============================================

En esta segunda versión expandirás la calculadora para que pueda realizar
las cuatro operaciones básicas: suma, resta, multiplicación y división.

Conceptos aplicados:
- Operadores aritméticos (+, -, *, /)
- Condicionales if/elif/else
- F-strings para formateo profesional
- Manejo básico de tipos numéricos

Instrucciones:
1. Pide dos números al usuario
2. Pregunta qué operación desea realizar
3. Usa if/elif/else para realizar la operación correspondiente
4. Muestra el resultado con f-strings formateados
"""

# TODO 1: Pide el primer número al usuario y conviértelo a float
# num1 = ...
num1 = float(input("Primer número: "))

# TODO 2: Pide el segundo número al usuario y conviértelo a float
# num2 = ...
num2 = float(input("Segundo número: "))

# TODO 3: Pregunta qué operación desea realizar
# Pista: input("¿Qué operación deseas realizar? (+, -, *, /): ")
# operacion = ...
operacion = input("¿Cuál de las operaciones quieres realizar? ¿Sumar, restar, multplicar o dividir?: ")

# TODO 4: Realiza la operación correspondiente usando if/elif/else
# Pista: Compara la variable 'operacion' con "+", "-", "*", "/"
#
# if operacion == "+":
#     resultado = num1 + num2
# elif operacion == "-":
#     ...
# elif operacion == "*":
#     ...
# elif operacion == "/":
#     ...
# else:
#     print("❌ Operación no válida")

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    resultado = num1 / num2
else:
    print("No es válida esa operación")
    resultado = None

# TODO 5: Muestra el resultado usando f-strings
# Pista: f"El resultado de {num1} {operacion} {num2} = {resultado:.2f}"
# El :.2f muestra solo 2 decimales
# print(f"...")
if resultado is not None:
    print(f"El resultado de {num1} {operacion} {num2} = {resultado:.2f}")

# ¡Perfecto! Ahora tu calculadora puede hacer las 4 operaciones básicas
#
# Ejemplos para probar:
# - 10 + 5 → debe dar 15.00
# - 10 - 3 → debe dar 7.00
# - 4 * 5 → debe dar 20.00
# - 10 / 3 → debe dar 3.33
# - 10 % 3 → (si pruebas una operación no válida, debe mostrar mensaje de error)
#
# 💡 Nota: Si intentas dividir por cero (10 / 0), Python mostrará un error.
#    Esto lo arreglaremos en la v3 con validación de entrada.
