"""Escritura y lectura básicas de archivos."""

ruta = "demo.txt"
with open(ruta, "w", encoding="utf-8") as f:
    f.write("Hola, archivo\n")

with open(ruta, "r", encoding="utf-8") as f:
    for i, linea in enumerate(f, start=1):
        print(f"{i}: {linea.strip()}")
