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
num1 = input("Introduce el primer número --> ")
float_num1 = float(num1)

# TODO 2: Pide el segundo número al usuario y conviértelo a float
# num2 = ...
num2 = input("Introduce el segundo número --> ")
float_num2 = float(num2)

# TODO 3: Pregunta qué operación desea realizar
# Pista: input("¿Qué operación deseas realizar? (+, -, *, /): ")
# operacion = ...
operacion = input("¿Qué operación desea realizar? (+, -, *, /) --> ")

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
    resultado = float_num1 + float_num2
elif operacion == "-":
    resultado = float_num1 - float_num2
elif operacion == "*":
    resultado = float_num1 * float_num2 
elif operacion == "/":
    resultado = float_num1 / float_num2
else:
    print("❌ Lo siento. No se reconoce la operación que ha introducido. Vuelva a intentarlo.")


# TODO 5: Muestra el resultado usando f-strings
# Pista: f"El resultado de {num1} {operacion} {num2} = {resultado:.2f}"
# El :.2f muestra solo 2 decimales
# print(f"...")
print(f"{float_num1} {operacion} {float_num2} = {round(resultado, 2)}")


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

