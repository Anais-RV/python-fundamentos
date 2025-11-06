# EJERCICIO AUTÓNOMO 2: Área del Rextángulo
# Enunciado: `area_rectangulo(a, b)`

# TODO 1: Crear la función 'area_rectangulo(a, b)'
def area_rectangulo(a, b):
    # TODO 1.1: Calcular el area (base X altura)
    area = a * b
    # TODO 1.2: Imprimir el area del rectángulo calculado
    return f"\nÁrea del rectángulo: {area}"

# TODO 2: Crear la función principal
def main():
    # TODO 2.1: Bucle 'while' para comprobar si han introducido bien los números
    while True:
        # TODO 2.2: Imprimir el título del ejercicio
        print("--- Área del rectángulo ---")
        # TODO 2.3: Verificar si se han introducido dos números usando try/except
        try:
            # TODO 2.4: Pedir la base del rectángulo
            base = float(input("\nEscribe la base del rectángulo --> "))
            # TODO 2.5: Pedir la altura del rectángulo
            altura = float(input("\nEscribe la altura del rectángulo --> "))

            # TODO 2.6: Imprimir la función con la base y la altura introducidos
            print(area_rectangulo(base, altura))
            # TODO 2.7: Terminar bucle 'while' al mostrar resultado
            break

        # TODO 2.7: Mostrar mensaje de error si uno de los dos valores no es un número
        except ValueError:
            print("\nERROR ❌. Sólo se permiten introducir números.")
            # TODO 2.8: Volver a empezar el bucle si no se han introducidos los datos correctos
            continue

# TODO 3: Punto de entrada del programa
if __name__ == "__main__":
    main()

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