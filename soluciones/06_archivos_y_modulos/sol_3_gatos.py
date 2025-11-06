import csv

# Datos de ejemplo
gatos = [
    ["Nombre", "Edad", "Raza", "Color"],
    ["Michi", 2, "Siames", "Crema"],
    ["Luna", 3, "Persa", "Blanco"],
    ["Simba", 1, "Bengalí", "Naranja"],
    ["Nala", 4, "Mestizo", "Gris"]
]

# 1️⃣ Escribir el archivo CSV
with open("gatos.csv", "w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerows(gatos)

# 2️⃣ Leer el archivo CSV y mostrar su contenido
with open("gatos.csv", "r", encoding="utf-8") as f:
    lector = csv.reader(f)
    for fila in lector:
        print(fila)

#print("\n".join(str(x) for x in gatos))