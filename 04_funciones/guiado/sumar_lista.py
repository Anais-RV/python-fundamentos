# Guiado 2: Sumar lista
# Enunciado: Crea `def sumar(nums):` que sume elementos y retorne el total. 
# Valida que `nums` sea lista.

# TODO 0: Imprime el título del ejercicio
print("--- Función Sumar Lista ---")

# TODO 1: Crear la funcion 'def sumar(nums)'
def sumar(nums):
    # TODO 2: Añadir suma de los números de la lista
    suma = 0
    # TODO 3: Iniciar bucle que recorra la lista de números
    for i in nums:
        # TODO 4: Imprimir numero actual y total actual
        print(f"\nNúmero actual: {i} | Suma actual: {suma}")
        print(f"Suma parcial: {i} + {suma} =")
        # TODO 5: Acumular suma con el numero recorrido e imprimir resultado
        suma += i
        print(f"{suma}")
    # TODO 6: Devolver la suma total
    return f"\n --- Suma total: {suma} ---"

# TODO 7: Declarar lista de números
nums = [9, 3, 2, 12]

# TODO 8: Punto de entrada del programa
if __name__ == "__main__":
    # TODO 9: Validar si 'nums' es una lista de números usando try/except
    try: 
        # TODO 9.5: Imprimir función con el resultado si sale True
        print(sumar(nums))
    # TODO 10: Mostrar mensaje de error si 'nums' no es una lista de números o si en la lista de números hay otro valor con diferente tipo de dato
    except TypeError:
        print("ERROR ❌. La variable 'nums' debe ser una lista de números.")