# EJERCICIO AUTÓNOMO 2: Combinación de listas
# Enunciado: Combina dos listas en un dict `{nombre: edad}`.

# TODO 1: Crear funcion principal
def main():
    # TODO 1.1: Imprimir título del ejercicio
    print("--- Combinación de listas ---")

    # TODO 1.2: Declarar 2 listas a combinar
    lista1 = ["nombre", "edad", "color"]
    lista2 = ["David", 25, "Verde"]

    # TODO 1.3: Declarar un diccionario que conjunte los dos listas
    # zip() --> Esta función toma las dos listas y las combina en una secuencia de tuplas,
    # donde cada tupla contiene un elemento de cada lista en la misma posición.
    # EJ: zip(["nombre"], ["edad"]) crea [('nombre', 'edad')]
    # dict() --> Esta función toma la iterable de tuplas y crea un diccionario a partir de él,
    # usando el primer elemento de cada tupla como la clave y el segundo como valor
    # EJ: dict(zip(["nombre"], ["edad"])) crea {'nombre': 'edad'}
    diccionario = dict(zip(lista1, lista2))

    # TODO 1.4: Imprimir las dos listas y el diccionario conjunto de dichas listas
    print(f"\nPrimera lista: {lista1}")
    print(f"\nSegunda lista: {lista2}")
    print(f"\nDiccionario conjunto entre dos listas: {diccionario}\n")

# TODO 2: Punto de entrada del programa
if __name__ == "__main__":
    main()

# RESULTADO:
# --- Combinación de listas ---
#
# Primera lista: ['nombre', 'edad', 'color']
# 
# Segunda lista: ['David', 25, 'Verde']
# 
# Diccionario conjunto entre dos listas: {'nombre': 'David', 'edad': 25, 'color': 'Verde'}
#
# -----------------------------------------------
# Éxito ✅