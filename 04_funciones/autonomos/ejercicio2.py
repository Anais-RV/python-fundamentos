# EJERCICIO AUTÓNOMO 2: Área del Rextángulo
# Enunciado: `area_rectangulo(a, b)`

# TODO 1: Crear la función 'area_rectangulo(a, b)'
def area_rectangulo(a, b):
    # TODO 2: Calcular el area (base X altura)
    area = a * b
    # TODO 3: Imprimir el area del rectnángulo calculado
    return f"\nÁrea del rectángulo: {area}"

# TODO 4: Punto de entrada del programa
if __name__ == "__main__":
    # TODO 4.5: Imprimir el título del ejercicio
    print("--- Área del rectángulo ---")
    # TODO 5: Verificar si se han introducido dos números usando try/except
    try:
        # TODO 6: Pedir la base del rectángulo
        base = float(input("\nEscribe la base del rectángulo --> "))
        # TODO 7: Pedir la altura del rectángulo
        altura = float(input("\nEscribe la altura del rectángulo --> "))

        # TODO 8: Imprimir la función con la base y la altura introducidos
        print(area_rectangulo(base, altura))

    # TODO 9: Mostrar mensaje de error si uno de los dos valores no es un número
    except ValueError:
        print("\nERROR ❌. Sólo se permiten introducir números.")

# EJEMPLO:
# --- Área del rectángulo ---
#
#Escribe la base del rectángulo --> 9
#
# Escribe la altura del rectángulo --> 4
#
# Área del rectángulo: 36.0
# ---------------------------------------
# Éxito ✅