# DESAFÍO DE BIGOTES FELICES: Filtro
# Enunciado: Dada una lista de gatos con edades, retorna sólo los mayores de 5 años.

# TODO 1: Crear funcion para recorrer lista de gatos
def listado(lista):
    # TODO 1.1: Imprimir titulo de lista actual
    print("\n--- Lista actual de gatos Bigotes Felices ---\n")

    # TODO 1.2: 'if/else' si existe la lista asignada en el parámetro
    if lista:
        # TODO 1.3: bucle 'for' para recorrer la lista
        for gato in lista:
            # TODO 1.4: Imprimir datos de la lista en formato de texto f-string
            print(f"Nombre: {gato['nombre']} | Edad: {gato['edad']} años")
        # TODO 1.5: Imprimir longitud de la lista en formato de texto f-string
        print(f"\nNúmero de gatos en la lista: {len(lista)}")
    # TODO 1.5: 'else' si no existe la lista de gatos
    else:
        print("No hay gatos en esa lista.")

# TODO 2: Crear función para filtrar gatos mayores de 5 años
def mayor_de_5(lista):
    # TODO 2.1: Crear lista vacía para agregar gatos filtrados
    gatos_mayores = []

    # TODO 2.2: 'if/else' si existe la lista asignada en el parámetro
    if lista:
        # TODO 2.3: Imprimir advertencia de filtrado
        print("\n--- Filtrando lista de gatos mayores de 5 años ---")
        # TODO 2.4: bucle 'for' para recorrer la lista
        for gato in lista:
            # TODO 2.5: filtrar gatos mayores de 5 años 
            if gato['edad'] > 5:
                # TODO 2.6: añadir gato mayor de 5 años en la lista 'gatos_mayores'
                gatos_mayores.append(gato)
        # TODO 2.7: Devolver la lista con los datos actualizados
        return gatos_mayores
    # TODO 2.8: 'else' si no existe la lista de gatos
    else:
        print("No hay una lista para filtrar.")

# TODO 3: Crear la función principal
def main():

    # TODO 3.1: Imprimir título del ejercicio
    print("--- BIGOTES FELICES (filtro) ---")
    # TODO 3.2: Crear lista de objetos con los datos de los gatos
    lista_gatos = [
        {"nombre": "Michi", "edad": 10},
        {"nombre": "Pelusa", "edad": 2},
        {"nombre": "Franky", "edad": 4},
        {"nombre": "Niko", "edad": 5},
        {"nombre": "Pachula", "edad": 7},
        {"nombre": "Simba", "edad": 8},
        {"nombre": "Chachito", "edad": 3}
    ]

    # TODO 3.3: Llamar la función 'listado(lista_gatos)'
    listado(lista_gatos)

    # TODO 3.4: Filtrar los gatos mayores de 5 años usando la función 'mayor_de_5(lista_gatos)'
    gatos_mayores = mayor_de_5(lista_gatos)

    # TODO 3.5: Volver a llamar la función 'listado()' con los gatos mayores de 5 años
    listado(gatos_mayores)

# TODO 4: Punto de entrada del programa
if __name__ == "__main__":
    main()

# RESULTADO:
# --- BIGOTES FELICES (filtro) ---
# 
# --- Lista actual de gatos Bigotes Felices ---
# 
# Nombre: Michi | Edad: 10 años
# Nombre: Pelusa | Edad: 2 años
# Nombre: Franky | Edad: 4 años
# Nombre: Niko | Edad: 5 años
# Nombre: Pachula | Edad: 7 años
# Nombre: Simba | Edad: 8 años
# Nombre: Chachito | Edad: 3 años
# 
# Número de gatos en la lista: 7
# 
# --- Filtrando lista de gatos mayores de 5 años ---
# 
# --- Lista actual de gatos Bigotes Felices ---
#
# Nombre: Michi | Edad: 10 años
# Nombre: Pachula | Edad: 7 años
# Nombre: Simba | Edad: 8 años
#
# Número de gatos en la lista: 3
# ---------------------------------------------------
# Éxito ✅ 
