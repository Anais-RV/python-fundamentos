"""
Calculadora v3 - Menú interactivo con validación
=================================================

En esta tercera versión añadirás un menú que se repite hasta que el usuario
decida salir, validación de entrada y control de errores (división por cero).

Conceptos aplicados:
- Bucle while para repetir el menú
- break para salir del bucle
- continue para volver al inicio del bucle
- Validación de entrada del usuario
- Control de división por cero

Instrucciones:
1. Crea un bucle while infinito
2. Muestra un menú numerado
3. Valida que la opción sea válida
4. Pide los números y realiza la operación
5. Controla la división por cero
6. Permite salir con la opción 5
"""

# TODO 1: Crea el bucle principal
# while True:
#     # Todo el código va aquí dentro
while True:

    # TODO 2: Muestra el menú
    # print("\n=== CALCULADORA ===")
    # print("1. Sumar")
    # print("2. Restar")
    # print("3. Multiplicar")
    # print("4. Dividir")
    # print("5. Salir")
    print("\n==== 💻 CALCULADORA 💻 ====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    # TODO 3: Pide la opción al usuario
    # opcion = input("\nElige una opción: ")
    opcion = input("\nElige una opción: ")

    # TODO 4: Si elige salir (opción 5), termina el programa
    # if opcion == "5":
    #     print("¡Hasta pronto! 👋")
    #     break  # Sale del bucle while
    if opcion == "5":
        print("¡Nos vemos pronto!")
        break

    # TODO 5: Valida que la opción sea válida (1, 2, 3 o 4)
    # if opcion not in ["1", "2", "3", "4"]:
    #     print("❌ Opción no válida. Intenta de nuevo.")
    #     continue  # Vuelve al inicio del bucle (muestra el menú de nuevo)
    if opcion not in ["1", "2", "3", "4"]:
        print("❌ Opción inválida. Vuelva a intentarlo.")
        continue

    # TODO 6: Pide los dos números
    # num1 = float(input("Primer número: "))
    # num2 = float(input("Segundo número: "))
    num1 = input("Introduce su primer número: ")
    num2 = input("Introduce su segundo número: ")

    # TODO 6.5: Validar si los dos números son de tipo float
    try:
        num1 = float(num1)
        num2 = float(num2)

        # TODO 7: Controla la división por cero
        # if opcion == "4" and num2 == 0:
        #     print("❌ Error: No se puede dividir por cero")
        #     continue  # Vuelve al menú sin hacer la operación
        if opcion == "4" and num2 == 0:
            print("❌ Error: No se puede dividir por 0")
            continue

        # TODO 8: Realiza la operación según la opción elegida
        # if opcion == "1":
        #     resultado = num1 + num2
        #     simbolo = "+"
        # elif opcion == "2":
        #     resultado = num1 - num2
        #     simbolo = "-"
        # elif opcion == "3":
        #     resultado = num1 * num2
        #     simbolo = "*"
        # elif opcion == "4":
        #     resultado = num1 / num2
        #     simbolo = "/"
        if opcion == "1":
            resultado = num1 + num2
            simbolo = "+"
        if opcion == "2":
            resultado = num1 - num2
            simbolo = "-"
        if opcion == "3":
            resultado = num1 * num2
            simbolo = "*"
        if opcion == "4":
            resultado = num1 / num2
            simbolo = "/"

        # TODO 9: Muestra el resultado con f-string
        # print(f"✅ {num1} {simbolo} {num2} = {resultado:.2f}")
        print(f"{num1} {simbolo} {num2} = {round(resultado, 2)}")

    # TODO 10: Muestra el mensaje de error usando except
    except ValueError:
        print(f"ERROR ❌. Uno de los valores introducidos (num1: {num1} | num2: {num2}) no es un número. Vuelva a intentarlo.")
        continue

# ¡Excelente trabajo! Ahora tienes una calculadora interactiva que:
# - Se repite hasta que el usuario quiera salir
# - Valida las opciones ingresadas
# - Controla la división por cero
# - Muestra mensajes claros con emojis
#
# Prueba estos casos:
# 1. Realiza varias operaciones seguidas sin salir
# 2. Intenta una opción inválida (ej: 9) → debe mostrar error y volver al menú
# 3. Intenta dividir por cero → debe mostrar error y volver al menú
# 4. Sal con la opción 5 → el programa debe terminar correctamente
#
# 💡 En la v4 organizarás todo este código en funciones para que sea más limpio
# --------------------------------------------------
# Primer test: calcular 4 como num1 y 5 como num2 con cualquier operacion
# Resultado: Éxito ✅ 
# --------------------------------------------------
# Segundo test: calcular 'hola' como num1 y 5 como num2 con cualquier operacion
# Resultado: Error ❌
# Motivo: ValueError: could not convert string to float: 'hola'
