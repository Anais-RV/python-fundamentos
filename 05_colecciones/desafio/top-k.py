# DESAFÍO DE BIGOTES FELICES: Top-K
# Enunciado: Dada una lista de pesos de gatos, muestra los 3 más pesados.

# TODO 1: Función que imprime el recorrido de la lista de gatos
def imprimir(gatos):

    for i, gato in enumerate(gatos, 1):
        print(f"{i}. Nombre: {gato['nombre']} | Peso: {gato['peso']} kg.")

# TODO 2: Función que ordena de mayor a menor peso la lista de gatos
def los_tres_pesados(gatos):

    print("\n--- Listando gatos de menor a mayor... ---")

    gatos_ordenados = sorted(gatos, key=lambda p:p['peso'], reverse=True)

    return gatos_ordenados

# TODO 3: Función que enumera los tres primeros gatos de una lista
def tres_primeros(gatos):
    print("\n--- Listando los tres primeros gatos más pesados... ---")

    top_3 = gatos[:3]

    return top_3

# TODO 4: Función principal del programa
def main():
    print("--- DESAFÍO BIGOTES FELICES: Top-K ---")

    gatos = [
        {"nombre": "Michi", "peso": 4.5},
        {"nombre": "Luna", "peso": 3.2},
        {"nombre": "Pelusa", "peso": 5.8},
        {"nombre": "Garfield", "peso": 7.3},
        {"nombre": "Simba", "peso": 4.1},
        {"nombre": "Nala", "peso": 6.2},
        {"nombre": "Tom", "peso": 3.8},
        {"nombre": "Felix", "peso": 5.5}
    ]

    print("\n--- Lista de gatos ---")

    imprimir(gatos)

    gatos_pesados = los_tres_pesados(gatos)

    print("\n--- Lista de gatos pesados de mayor a menor ---")

    imprimir(gatos_pesados)

    top_tres = tres_primeros(gatos_pesados)

    print("\n--- 👑 Top 3 Gatos Pesados 👑 ---")

    imprimir(top_tres)

# TODO 5: Punto de entrada del programa
if __name__ == "__main__":
    main()