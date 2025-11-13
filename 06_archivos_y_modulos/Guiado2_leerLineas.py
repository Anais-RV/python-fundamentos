#2. Crea un módulo `utiles.py` con `leer_lineas(ruta)` y `guardar_lineas(ruta, lineas)`.

#leer y mostrar
ruta="./escribir.txt"
print("Mostrar los datos leidos:\n")
with open(ruta, "r", encoding="utf-8") as x:
    for i, linea in enumerate(x, start=1):
        print(f"  {linea.strip()}")