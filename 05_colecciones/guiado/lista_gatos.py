# EJERCICIO GUIADO 1: Lista de gatos
# ENUNCIADO: Crea una lista con 3 nombres y recórrela imprimiendo índices y valores.

# TODO 1: Crear lista de gatos 
lista_gatos = ["Niko", "Michi", "Chachito"]

# TODO 2: Crear función principal
def main():
    # TODO 2.1: Imprimir título del ejercicio
    print("--- Lista de gatos ---")

    # TODO 2.2: Iterar sobre la lista con enumerate()
    for i, gato in enumerate(lista_gatos, 1):
        print(f"{i}: {gato}")

# TODO 3: Punto de entrada del programa
if __name__ == "__main__":
    main()

# RESULTADO:
# --- Lista de gatos ---
# 1: Niko
# 2: Michi
# 3: Chachito
# -----------------------
# Éxito ✅ 