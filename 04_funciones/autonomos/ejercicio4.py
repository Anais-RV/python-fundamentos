# EJERCICIO AUTÓNOMO 4: Promedio de números
# Enunciado: `promedio(nums)` con manejo de lista vacía

# TODO 1: Crear la función 'promedio(nums)'
def promedio(nums):

    # TODO 1.2: Añadir una suma acumulable para la lista
    suma = 0

    # TODO 1.3: Agregar bucle 'while' para añadir números en la lista hasta introducir 0
    while True:
        # TODO 1.4: Verificar si el valor introducido es un número usando try/except
        try:
            # TODO 1.4.1: Pedir un número al usuario
            num = int(input("\nIntroduce un número (0 para terminar) --> "))

            # TODO 1.4.2: No agregar a la lista si el numero es menor que 0
            if num < 0:
                print("ERROR ❌. Introduce un número mayor que 0.")
                continue

            # TODO 1.4.3: Terminar bucle si el número es 0
            if num == 0:
                print("Fin de bucle!!")
                break

            # TODO 1.4.4: Añadir número introducido a la lista
            nums.append(num)

            # TODO 1.4.5: Imprimir lista actual
            print(f"Lista: {nums}")

            # TODO 1.4.6: Acumular la suma de los valores de la lista e imprimir
            print(f"Suma parcial: {suma} + {num} = ")
            suma += num
            print(suma)

            # TODO 1.4.7: Imprimir longitud de la lista actual
            longitud = len(nums)
            print(f"Longitud de la lista actual: {longitud}")

        # TODO 1.5: Mostrar mensaje de error si el valor introducido no es un número
        except ValueError:
            print("ERROR ❌. Número no válido.")
            continue

    # TODO 1.6: Imprimir resumen de la lista al finalizar el bucle
    print("\nResumen")
    print(f"Lista: {nums} | Suma total: {suma} | Longitud: {longitud}")

    # TODO 1.7: Calcular el promedio de la lista e imprimirlo
    medio = suma / longitud
    return  f"\nCálculo promedio: {medio:.2f}"

# TODO 2: Crear la función principal
def main():
    # TODO 2.1: Imprimir título del ejercicio
    print("--- Promedio de lista de números ---")
    # TODO 2.2: Agregar lista vacía para dar forma a la función
    nums = []
    # TODO 2.3: Imprimir función con la lista vacía
    print(promedio(nums))

# TODO 3: Punto de entrada del programa
if __name__ == "__main__":
    main()

# EJEMPLO:
# --- Promedio de lista de números ---
#
# Introduce un número (0 para terminar) --> 2
# Lista: [2]
# Suma parcial: 0 + 2 =
# 2
# Longitud de la lista actual: 1
# 
# Introduce un número (0 para terminar) --> 7
# Lista: [2, 7]
# Suma parcial: 2 + 7 =
# 9
# Longitud de la lista actual: 2
# 
# Introduce un número (0 para terminar) --> 1
# Lista: [2, 7, 1]
# Suma parcial: 9 + 1 =
# 10
# Longitud de la lista actual: 3
#
# Introduce un número (0 para terminar) --> 0
# Fin de bucle!!
#
# Resumen
# Lista: [2, 7, 1] | Suma total: 10 | Longitud: 3
#
# Cálculo promedio: 3.33
# ------------------------------------------------
# Éxito ✅ #    