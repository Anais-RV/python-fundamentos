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

while True:
    
    
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    
    opcion = input("\nElige una opción: ")
    
    if opcion == "5":
        print("¡Hasta pronto! 👋")
        break  

    
    if opcion not in ["1", "2", "3", "4"]:
        print("❌ Opción no válida. Intenta de nuevo.")
        continue 

    
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))

   
    if opcion == "4" and num2 == 0:
        print("❌ Error: No se puede dividir por cero")
        continue  

   
    if opcion == "1":
        resultado = num1 + num2
        simbolo = "+"
    elif opcion == "2":
        resultado = num1 - num2
        simbolo = "-"
    elif opcion == "3":
        resultado = num1 * num2
        simbolo = "*"
    elif opcion == "4":
        resultado = num1 / num2
        simbolo = "/"

    
    print(f"✅ {num1} {simbolo} {num2} = {resultado:.2f}")


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