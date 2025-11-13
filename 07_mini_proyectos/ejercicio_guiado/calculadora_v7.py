"""
Calculadora v7 - Refactorización con Operador Morsa
====================================================

Esta versión refactoriza la v6 aplicando el operador morsa (:=) para:
- Reducir código repetitivo
- Mejorar la legibilidad en validaciones
- Aplicar sintaxis moderna de Python 3.8+

Conceptos aplicados:
- Operador morsa (:=) en bucles while
- Operador morsa en condicionales
- Operador morsa en validaciones
- Refactorización de código existente

Instrucciones:
1. Lee la guía completa: ejercicio_guiado/GUIA.md
2. Lee el cheat sheet: cheatsheets/07_operador_morsa.md
3. Completa los TODOs aplicando el operador morsa
4. Compara con la v6 para ver las mejoras
"""

import json
import os

# Nombre del archivo donde se guardará el historial
ARCHIVO_HISTORIAL = "historial_calculadora.json"

# Lista global para el historial
historial = []


# ===== FUNCIONES DE OPERACIONES =====

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
    print("5. Ver historial")
    print("6. Limpiar historial")
    print("7. Salir")


def obtener_numeros():
    """Pide dos números al usuario con validación mejorada."""

    # TODO 1: Refactoriza usando operador morsa
    # Combina el input y la validación en una sola expresión
    # Pista: while not (entrada := input(...)).algo():

    while True:
        entrada1 = input("Primer número: ")
        try:
            num1 = float(entrada1)
            break
        except ValueError:
            print("❌ Ingresa un número válido")

    while True:
        entrada2 = input("Segundo número: ")
        try:
            num2 = float(entrada2)
            break
        except ValueError:
            print("❌ Ingresa un número válido")

    return num1, num2


# ===== FUNCIONES DE HISTORIAL (memoria) =====

def guardar_operacion(num1, num2, operacion, resultado):
    """Guarda una operación en el historial (en memoria)."""
    operacion_dict = {
        "num1": num1,
        "num2": num2,
        "operacion": operacion,
        "resultado": resultado
    }
    historial.append(operacion_dict)


def mostrar_historial():
    """Muestra todas las operaciones del historial."""
    if not historial:
        print("📭 No hay operaciones en el historial")
        return

    print("\n📜 HISTORIAL DE OPERACIONES:")
    for i, op in enumerate(historial, 1):
        print(f"{i}. {op['num1']} {op['operacion']} {op['num2']} = {op['resultado']:.2f}")


# ===== FUNCIONES DE PERSISTENCIA (archivos JSON) =====

def cargar_historial():
    """Carga el historial desde el archivo JSON.

    Returns:
        Lista con el historial cargado, o lista vacía si no existe el archivo.
    """
    try:
        with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            print(f"✅ Historial cargado: {len(datos)} operaciones")
            return datos
    except FileNotFoundError:
        print("📝 No hay historial previo, iniciando uno nuevo")
        return []
    except json.JSONDecodeError:
        print("⚠️  Archivo de historial corrupto, iniciando uno nuevo")
        return []


def guardar_historial_archivo():
    """Guarda el historial actual en el archivo JSON."""
    try:
        with open(ARCHIVO_HISTORIAL, "w", encoding="utf-8") as archivo:
            json.dump(historial, archivo, indent=2, ensure_ascii=False)
        print("✅ Historial guardado correctamente")
    except Exception as e:
        print(f"❌ Error al guardar el historial: {e}")


def limpiar_historial():
    """Limpia el historial en memoria y elimina el archivo."""
    global historial

    # TODO 2: Refactoriza la confirmación con operador morsa
    # Pista: if (confirmacion := input(...).lower()) != "s":
    
    if (confirmacion := input("⚠️  ¿Estás seguro de que quieres limpiar el historial? (s/n): ").lower()) != "s":
        print("❌ Operación cancelada")
        return

    historial = []

    try:
        if os.path.exists(ARCHIVO_HISTORIAL):
            os.remove(ARCHIVO_HISTORIAL)
        print("🗑️  Historial limpiado correctamente")
    except Exception as e:
        print(f"❌ Error al eliminar el archivo: {e}")


# ===== FUNCIÓN PRINCIPAL =====

def main():
    """Función principal de la calculadora."""
    global historial

    print("🔄 Cargando historial...")
    historial = cargar_historial()

    while True:
        mostrar_menu()

        # TODO 3: Considera si puedes usar operador morsa aquí
        # ¿Se puede combinar mostrar_menu() y input() de alguna manera?

        if (opcion := input("\nElige una opción: ")) == "7":
            print("💾 Guardando historial...")
            guardar_historial_archivo()
            print("¡Hasta pronto! 👋")
            break

        if (opcion := input("\nElige una opción: ")) == "5":
            mostrar_historial()
            continue

        if (opcion := input("\nElige una opción: ")) == "6":
            limpiar_historial()
            continue

        # TODO 4: Refactoriza esta validación con operador morsa
        # Pista: Convierte la opción a número y valida en una sola expresión
        if (opcion := int(input("\nElige una opción: "))) not in ["1", "2", "3", "4"]:
            print("❌ Opción no válida")
            continue

        try:
            num1, num2 = obtener_numeros()
        except ValueError:
            print("❌ Error al procesar los números")
            continue

        if opcion == "4" and num2 == 0:
            print("❌ No se puede dividir por cero")
            continue

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

        print(f"✅ {num1} {simbolo} {num2} = {resultado:.2f}")
        guardar_operacion(num1, num2, simbolo, resultado)


if __name__ == "__main__":
    main()


# 🦭 REFLEXIÓN FINAL
#
# Después de completar esta refactorización, pregúntate:
#
# 1. ¿El código es más legible ahora o era mejor antes?
# 2. ¿Dónde el operador morsa realmente ayudó?
# 3. ¿Hay algún lugar donde lo usaste y NO debiste?
#
# El operador morsa es una herramienta, no un objetivo.
# Úsalo solo cuando mejore el código, no solo porque puedas.
#
# 💡 Comparación de líneas de código:
# - v6: ~250 líneas
# - v7: ~220 líneas (con operador morsa bien aplicado)
#
# ¡La refactorización no se trata solo de reducir líneas,
# sino de mejorar la claridad y mantenibilidad!
