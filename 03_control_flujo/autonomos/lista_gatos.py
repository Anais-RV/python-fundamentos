# EJERCICIO AUTÓNOMO 1: Lista de gatos
# Enunciado: Recorre una lista de gatos y imprime sus nombres.

# TODO 0: Imprimir título del programa
print("---- LISTA DE GATOS ----")
# TODO 1: Declarar array con nombres de gatos
gatos = ["Michi", "Leo", "Nico", "Fluffy", "Pimpi"]
# TODO 2: Imprimir nombres de gatos dentro del array
print(f"Nombres de gatos: {gatos}\n")

# TODO 3: Iniciar bucle for que recorra el array de gatos con su longitud
print(f"Lista:")
for i in range(len(gatos)):
    # TODO 4: Imprimir nombres de gatos hasta que no queden más nombres
    print(f"Gato nº{i+1} --> {gatos[i]}")

# Arranque del programa: python lista_gatos.py
# --------------------------------------------
# Resultado:
# ---- LISTA DE GATOS ----
# Nombres de gatos: ['Michi', 'Leo', 'Nico', 'Fluffy', 'Pimpi']

# Lista:
# Gato nº1 --> Michi
# Gato nº2 --> Leo
# Gato nº3 --> Nico
# Gato nº4 --> Fluffy
# Gato nº5 --> Pimpi