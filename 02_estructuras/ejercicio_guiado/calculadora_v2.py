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
print("Valor 1:")
first_input = input()
num1 = int(first_input)

# TODO 2: Pide el segundo número al usuario y conviértelo a float
# num2 = ...
print("Valor 2:")
second_input = input()
num2 = int(second_input)

# TODO 3: Pregunta qué operación desea realizar
# Pista: input("¿Qué operación deseas realizar? (+, -, *, /): ")
# operacion = ...
print("¿Operación a realizar?")
print("0 - Salir")
print("1 - [+] Sumar")
print("2 - [-] Restar")
print("3 - [x] Multiplicar")
print("4 - [%] Dividir")
user_sel = input()

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

# TODO 5: Muestra el resultado usando f-strings
# Pista: f"El resultado de {num1} {operacion} {num2} = {resultado:.2f}"
# El :.2f muestra solo 2 decimales
# print(f"...")


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
if user_sel == "0":
  print("Ten un buen día.")
  exit()
elif user_sel == "1":
  print(f"{num1 + num2}")
  exit()
elif user_sel == "2":
  print(f"{num1 - num2}")
  exit()
elif user_sel == "3":
  print(f"{num1 * num2}")
  exit()
elif user_sel == "4":
  print(f"{num1 / num2}")
  exit()
else:
  print("Operación no válida")
  exit()