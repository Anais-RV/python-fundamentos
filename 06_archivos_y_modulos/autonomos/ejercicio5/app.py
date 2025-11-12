# app.py
# Script para utilizar las funciones de 'utiles.py'

# TODO 1: Importar funciones de utiles
from utiles import leer_lineas, guardar_lineas

# TODO 2: Imprimir título de app.py
print("--- APP ---")

while True: 
    # TODO 3: Pedir al usuario un nombre para el archivo
    ARCHIVO = input("\nEscribe un nombre para el archivo a guardar datos --> ")

    if len(ARCHIVO) == 0:
        print("❌ No hay nombre de archivo.")
        continue

    if not ARCHIVO.isalpha():
        print("❌ Sólo se imprime letras (no valen números ni símbolos).")
        continue

    ARCHIVOTXT = ARCHIVO + ".txt"

    print("\nNombre de archivo validado ✅")

    print("\n--- Lista a imprimir datos ---")
    lista_gatos = [
        "Michi",
        "Simba",
        "Niko",
        "Leo",
        "Chuski"
    ]

    for gato in lista_gatos:
        print(gato)

    guardar_lineas(ARCHIVOTXT, lista_gatos)

    leer_lineas(ARCHIVOTXT)
    
    break
