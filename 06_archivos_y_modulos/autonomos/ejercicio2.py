# EJERCICIO AUTÓNOMO 2: Módulo 'utiles.py'
# Enunciado: Crea un módulo `utiles.py` con `leer_lineas(ruta)` y `guardar_lineas(ruta, lineas)`.

# TODO 1: Importamos las funciones del módulo 'utiles.py'
from utiles import leer_lineas, guardar_lineas

# TODO 2: Ejemplo Nº 1 de lista de tareas
print("\nEjemplo 1 de guardar tareas:")

# Definimos lista de tareas
tareas = [
    "Estudiar Python",
    "Hacer la cama",
    "Comer cachopo"
]

# Definimos nombre de archivo txt
archivoTxt = "tarea.txt"

# Función para guardar las líneas de la lista en el archivo txt
guardar_lineas(archivoTxt, tareas)

# Función que lee las líneas en el archivo txt
leer_lineas(archivoTxt)

# TODO 2: Ejemplo Nº2 de registro de gatos
print("\nEjemplo 2 de registro de gatos:")

# Definimos lista de gatos
gatos = [
    "Leo - 6 años - 5.6 kg",
    "Niko - 5 años - 6.5 kg",
    "Chachito - 7 años - 7.0 kg"
]

# Definimos nombre de archivo txt
gatosTxt = "gatos.txt"

# Función para guardar las líneas de la lista en el archivo txt
guardar_lineas(gatosTxt, gatos)

# Función de lectura de líneas de los gatos en el archivo txt
leer_lineas(gatosTxt)

# Comprobar la lista de gatos
if gatos:
    print(f"\nRegistro de gatos ({len(gatos)} gatos):")
    for gato in gatos:
        print(f"  🐱 {gato}")
