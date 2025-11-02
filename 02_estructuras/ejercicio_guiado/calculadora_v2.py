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

# TODO 2: Pide el segundo número al usuario y conviértelo a float
# num2 = ...
num2 = input("Introduce el segundo número --> ")

# TODO 3: Pregunta qué operación desea realizar
# Pista: input("¿Qué operación deseas realizar? (+, -, *, /): ")
# operacion = ...
operacion = input("¿Qué operación desea realizar? (+, -, *, /) --> ")

# TODO 3.5: Realiza try/except por si surge error al introducir números dados
try:
    float_num1 = float(num1)
    float_num2 = float(num2)

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

# Añadir dos mensajes de error
except ValueError:
    print(f"❌ Inválido. Uno de los números introducidos (num1: {num1} | num2: {num2}) es incorrecto.")
    print(f"Por favor, reinicie el programa. 🛠️")
except NameError:
    print(f"❌ No ha generado el resultado que esperaba.")
    print(f"Por favor, reinicie el programa. 🛠️")


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

# Primer test: introducir 5 como num1, 3 como num2 y cualquier signo sugerido en operador
# --------------------------------------------------
# Operador '+':
# Introduce el primer número --> 5
# Introduce el segundo número --> 3
# ¿Qué operación desea realizar? (+, -, *, /) --> +
# 5.0 + 3.0 = 8.0
# --------------------------------------------------
# Operador '-':
# Introduce el primer número --> 5
# Introduce el segundo número --> 3
# ¿Qué operación desea realizar? (+, -, *, /) --> -
# 5.0 - 3.0 = 2.0 
# --------------------------------------------------
# Operador '*':
# Introduce el primer número --> 5
# Introduce el segundo número --> 3
# ¿Qué operación desea realizar? (+, -, *, /) --> *
# 5.0 * 3.0 = 15.0
# --------------------------------------------------
# Operador '/':
# Introduce el primer número --> 5
# Introduce el segundo número --> 3
# ¿Qué operación desea realizar? (+, -, *, /) --> /
# 5.0 / 3.0 = 1.67  
# --------------------------------------------------
# Cualquier otro operador '%, (, )...':
# Introduce el primer número --> 5
# Introduce el segundo número --> 3
# ¿Qué operación desea realizar? (+, -, *, /) --> %
# ❌ Lo siento. No se reconoce la operación que ha introducido. Vuelva a intentarlo.
# --------------------------------------------------
# Éxito ✅ 
# --------------------------------------------------
# Segundo test: introducir un string en uno de los dos números que piden al usuario.
# --------------------------------------------------
# Probar con dato 'hola':
# Introduce el primer número --> hola
# ERROR ❌
# Motivo: ValueError: could not convert string to float: 'hola'
# --------------------------------------------------
# Tercer test: al agregar try/except, volver a ingresar 'hola' por si surge el mensaje.
# --------------------------------------------------
# Introduce el primer número --> hola
# Introduce el segundo número --> 3
# ¿Qué operación desea realizar? (+, -, *, /) --> +
# ❌ Inválido. Uno de los números introducidos (num1: hola | num2: 3) es incorrecto.
# Por favor, reinicie el programa. 🛠️
# --------------------------------------------------
# Mensaje mostrado con éxito ✅
