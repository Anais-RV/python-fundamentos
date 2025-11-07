"""
Calculadora v5 - Historial de operaciones
==========================================

En esta quinta versión añadirás un historial que guarda todas las operaciones
realizadas durante la sesión usando listas y diccionarios.

Conceptos aplicados:
- Listas para almacenar múltiples elementos
- Diccionarios para estructurar datos
- append() para añadir a listas
- enumerate() para iterar con índice
- Verificación de listas vacías

Instrucciones:
1. Crea una lista para almacenar operaciones
2. Crea función para guardar operaciones en el historial
3. Crea función para mostrar el historial
4. Añade opción "Ver historial" al menú
"""

# ===== FUNCIONES DE OPERACIONES (copiadas de v4) =====

def sumar(a, b):
    """Suma dos números."""
    return a + b


def restar(a, b):
    """Resta dos números."""
    return a - b


def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b


def dividir(a, b):
    """Divide dos números."""
    return a / b


# ===== FUNCIONES DE INTERFAZ =====

def mostrar_menu():
    """Muestra el menú de opciones de la calculadora."""
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Ver historial")  # Nueva opción
    print("6. Salir")  # Ahora es la opción 6


def obtener_numeros():
    """Pide dos números al usuario y los devuelve."""
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))
    return num1, num2


# ===== NUEVAS FUNCIONES PARA HISTORIAL =====

# TODO 1: Crea una lista global para almacenar el historial
# (Nota: en programación avanzada evitamos globales, pero aquí es didáctico)
# historial = []
historial = []

def guardar_operacion(num1, num2, operacion, resultado):
    """Guarda una operación en el historial.

    Args:
        num1: Primer número
        num2: Segundo número
        operacion: Símbolo de la operación (+, -, *, /)
        resultado: Resultado de la operación
    """
      
    # TODO 2: Crea un diccionario con los datos de la operación
    # operacion_dict = {
    #     "num1": num1,
    #     "num2": num2,
    #     "operacion": operacion,
    #     "resultado": resultado
    # }
    

    # TODO 3: Añade el diccionario a la lista historial
    # historial.append(operacion_dict)

    pass
    operacion_dict = {
        "num1": num1,
        "num2": num2,
        "operacion": operacion,
        "resultado": resultado
    }
    historial.append(operacion_dict)



def mostrar_historial():
    """Muestra todas las operaciones del historial."""
    # TODO 4: Verifica si el historial está vacío
    # if not historial:
    #     print("📭 No hay operaciones en el historial")
    #     return

    # TODO 5: Muestra el título
    # print("\n📜 HISTORIAL DE OPERACIONES:")

    # TODO 6: Itera sobre el historial con enumerate()
    # enumerate() nos da el índice (i) y el elemento (op)
    # El segundo parámetro (1) indica que empiece a contar desde 1
    # for i, op in enumerate(historial, 1):
    #     print(f"{i}. {op['num1']} {op['operacion']} {op['num2']} = {op['resultado']:.2f}")

    pass
    if not historial:
        print("No hay operaciones en el historial")
        return
    print("\nHistorial de operaciones")
    for i, op in enumerate(historial, 1):
            print(f"{i}. {op['num1']} {op['operacion']} {op['num2']} = {op['resultado']:.2f}")

# ===== FUNCIÓN PRINCIPAL =====

def main():
    """Función principal de la calculadora."""

    # while True:
        # mostrar_menu()
        # opcion = input("\nElige una opción: ")

        # TODO 7: Actualiza la condición de salir (ahora es la opción 6)
        # if opcion == "6":
        #     print("¡Hasta pronto! 👋")
        #     break

        # TODO 8: Añade la nueva opción 5 para ver el historial
        # if opcion == "5":
        #     mostrar_historial()
        #     continue  # Vuelve al menú sin pedir números

        # TODO 9: Actualiza la validación (ahora hay 5 opciones válidas)
        # if opcion not in ["1", "2", "3", "4", "5"]:
        #     print("❌ Opción no válida")
        #     continue

        # num1, num2 = obtener_numeros()

        # if opcion == "4" and num2 == 0:
        #     print("❌ No se puede dividir por cero")
        #     continue

        # TODO 10: Realiza la operación y guarda en el historial
        # if opcion == "1":
        #     resultado = sumar(num1, num2)
        #     simbolo = "+"
        # elif opcion == "2":
        #     resultado = restar(num1, num2)
        #     simbolo = "-"
        # elif opcion == "3":
        #     resultado = multiplicar(num1, num2)
        #     simbolo = "*"
        # elif opcion == "4":
        #     resultado = dividir(num1, num2)
        #     simbolo = "/"

        # print(f"✅ {num1} {simbolo} {num2} = {resultado:.2f}")

        # TODO 11: Guarda la operación en el historial
        # guardar_operacion(num1, num2, simbolo, resultado)

    pass
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ")
        if opcion == "6":
            print("¡See you soon!")
            break
        if opcion == "5":
            mostrar_historial()
            continue
        if opcion not in ["1", "2", "3", "4"]:
            print("Opción no válida")
            continue
        
        num1, num2 = obtener_numeros()
        
        if opcion == "4" and num2 == 0:
            print("No se puede dividir entre cero...")
            
        if opcion == "1":
            resultado = sumar(num1, num2)
            simbolo = "+"
        elif opcion == "2":
            resultado = restar(num1, num2)
            simbolo = "-"
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
            simbolo = "*"
        elif opcion == "4":
            resultado = dividir(num1, num2)
            simbolo = "/"
            
        print(f"{num1} {simbolo} {num2} ? {resultado:.2f}")

if __name__ == "__main__":
    main()


# ¡Fantástico! Ahora tu calculadora tiene memoria.
#
# Prueba estos casos:
# 1. Realiza varias operaciones (5 + 3, 10 - 4, 7 * 2, 15 / 3)
# 2. Elige "Ver historial" → debe mostrar todas las operaciones
# 3. Realiza más operaciones y vuelve a ver el historial → deben aparecer
# 4. Sal del programa y vuelve a ejecutarlo → el historial se habrá borrado
#    (es normal, en v6 lo guardaremos en un archivo para que persista)
#
# Ventajas de esta versión:
# ✅ Guarda todas las operaciones de la sesión
# ✅ Puedes revisar qué has calculado
# ✅ Usa estructuras de datos complejas (lista de diccionarios)
# ✅ Es fácil añadir más funcionalidades (ej: buscar, borrar operaciones)
#
# 💡 En la v6 guardarás el historial en un archivo JSON para que persista
