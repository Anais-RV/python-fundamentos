# EJERCICIO AUTÓNOMO 4: Slicing y comprehensions simples de listas.
# Enunciado: Slicing y comprensiones simples de listas.

# TODO 1: Función que muestra contenido de slicing
def slicing(lista, texto):
    print(f"\n--- Slicing de la lista --> {lista} ---")

    print("\nSintaxis de Slicing: lista[inicio:fin:paso]")

    # Slicing básico --> lista[inicio:fin]
    print("\nEjemplos de slicing básicos (lista[inicio:fin])")

    print(f"\nNúmeros [2:6]: {lista[2:6]}") # Del índice 2 hasta el 5 (6 no incluído)
    print(f"Números [:4]: {lista[:4]}") # Desde el principio hasta el índice 3
    print(f"Números [5:]: {lista[5:]}") # Desde el índice 5 hasta el final
    print(f"Números [-3:]: {lista[-3:]}") # Los 3 últimos índices
    print(f"Números [:-4]: {lista[:-4]}") # La lista excepto los 4 últimos índices

    # Slicing con paso --> lista[inicio:fin:paso]
    print("\nEjemplos de slicing con paso (lista[inicio:fin:paso])")

    print(f"\nNúmeros [::2]: {lista[::2]}") # Todos, pero de 2 en 2
    print(f"Números [3::2]: {lista[3::2]}") # Desde el índice 3, de 2 en 2
    print(f"Números [::-1]: {lista[::-1]}") # Invertir la lista

    print(f"\n--- Slicing del texto --> {texto} ---")
    print(f"String [0:6]: {texto[0:11]}") # Me encantan
    print(f"String [12:]: {texto[12:]}") # los cachopos
    print(f"String [::-1]: {texto[::-1]}") # Invierte el texto

# TODO 2: Funcion que muestra contenido de compresiones
def comprensiones(lista, texto):
    print(f"\n--- Comprensiones de la lista --> {lista} ---")

    print("\nFormato de las comprensiones: [expresion for elemento in lista]")

    print("\nEjemplos básicos:")

    print("\n1. Formato: [numero * 2 for numero in lista]")
    dobles = [numero * 2 for numero in lista]
    print(f"Lista de números multiplicados por dos: {dobles}")

    print("\n2. Formato: [numero ** 2 for numero in lista]")
    cuadrados = [numero ** 2 for numero in lista]
    print(f"Lista de números al cuadrado: {cuadrados}")

    print("\nEjemplos con condición --> Formato: [expresion for elemento in lista if condicion]")

    print("\n1. Formato: [numero for numero in lista if numero % 2 == 0]")
    pares = [numero for numero in lista if numero % 2 == 0]
    print(f"Lista de números pares: {pares}")

    print("\n2. Formato: [numero ** 3 for numero in lista if numero % 2 != 0]")
    imparescubos = [numero ** 3 for numero in lista if numero % 2 != 0]
    print(f"Lista de números impares al cubo: {imparescubos}")


def main():
    print("--- Slicing y compresiones simples de listas ---")

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    texto = "Me encantan los cachopos"

    print(f"\nLista predeterminada: {lista}")
    print(f"Texto predefinido: {texto}")

    while True:

        print("\n1. Slicing de la lista")
        print("2. Compresiones simples de la lista")
        print("3. Salir")

        try:
            opcion = int(input("\nElige una opcion --> "))

            if opcion == 1:
                print("Opción 1 confirmada!!")
                slicing(lista, texto)
                continue
            elif opcion == 2:
                print("Opcion 2 confirmada!!")
                comprensiones(lista, texto)
                continue
            elif opcion == 3:
                print("Opcion 3 confirmada!! Que tenga buen día!! ✨")
                break
            else:
                print("❌ Opción no válida")
                continue

        except ValueError:
            print("❌ Opción no válida")
            continue


# TODO 4: Punto de entrada del programa
if __name__ == "__main__":
    main()