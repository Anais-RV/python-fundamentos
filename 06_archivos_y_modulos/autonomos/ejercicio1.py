# EJERCICIO AUTÓNOMO 1: Gatos CVS
# Enunciado: Guarda un resumen de gatos en `gatos.csv` (separado por comas).

# Variables previos
# TODO 1: Declaramos una lista de diccionarios que almacenan una lista de gatos
lista_gatos = [
    {"nombre": "Michi", "edad": 3, "peso": 4.5, "color": "Naranja"},
    {"nombre": "Luna", "edad": 7, "peso": 3.2, "color": "Blanco"},
    {"nombre": "Pelusa", "edad": 2, "peso": 5.8, "color": "Gris"},
    {"nombre": "Garfield", "edad": 8, "peso": 7.3, "color": "Naranja"},
    {"nombre": "Simba", "edad": 5, "peso": 4.1, "color": "Marrón"},
    {"nombre": "Nala", "edad": 10, "peso": 6.2, "color": "Negro"},
    {"nombre": "Tom", "edad": 4, "peso": 3.8, "color": "Gris"}
]

# TODO 2: Recorremos la lista de gatos que queremos guardar en el archivo csv
print("--- Gatos a guardar ---")
for i, gato in enumerate(lista_gatos, 1):
    print(f"{i}. Nombre: {gato['nombre']} | Edad: {gato['edad']} años | Peso: {gato['peso']} kg | Color: {gato['color']}")

# Guardar información en formato CSV
# TODO 1: Empezamos primero por importar el módulo csv
import csv

# TODO 2: Crear y Escribir el contenido del archivo 'gatos.csv'
try:
    print("\nCreando archivo...")
    # TODO 2.1: Abrir archivo con permiso de escritura ("w")
    # newline="" --> siempre se usa con archivo CSV para evitar problemas con los saltos de línea
    # encoding="utf-8" --> evita problemas de codificación en el diccionario
    with open("gatos.csv", "w", newline="", encoding="utf-8") as archivo:

        # Definimos nombres de las columnas
        campos = ["nombre", "edad", "peso", "color"]
        # Creamos el escritor CSV
        # csv.DictWriter --> Objeto "escritor" especializado para escribir diccionarios en formato CSV
        # archivo --> 1º parámetro con el archivo abierto donde se escribirá
        # fieldnames=campos --> 2º parámetro con la lista con los nombres de las columnas del CSV 
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        # Escribimos la cabecera
        # writeheader() --> Escribe la primera línea del CSV con los nombres de las columnas (la cabecera)
        # Resultado -->  nombre,edad,peso,color
        # ⚠️ Importante: Solo se llama UNA vez al inicio.
        escritor.writeheader()

        # Escribimos todas las filas
        # writerows(lista_gatos) --> Escribe múltiples filas a la vez.
        # Toma una lista de diccionarios y escribe cada uno como una línea del CSV 
        # RESULTADO:
        # Michi,3,4.5,Naranja
        # Luna,7,3.2,Blanco
        # ...
        escritor.writerows(lista_gatos)

    print("\n✅ Archivo 'gatos.csv' creado con éxito con módulo csv!")
except Exception as e:
    print(f"❌ Hay un error al guardar datos: {e}")

# TODO 3: Leer y Mostrar el contenido del archivo csv creado
try:
    print("\nLeyendo archivo...")
    with open("gatos.csv", "r", encoding="utf-8") as archivo:
        # Leeremos el contenido del archivo
        contenido = archivo.read()
        print(f"\n{contenido}")

    with open("gatos.csv", "r", encoding="utf-8") as archivo:
        # Contamos las líneas (gatos + cabecera)
        lineas = archivo.readlines()
        print(f"Total de líneas: {len(lineas)}")
        print(f"Total de gatos guardados: {len(lineas) - 1}")

    print("\n✅ Archivo leído correctamente.")


except FileNotFoundError:
    print("❌ Archivo no encontrado.")
except Exception as e:
    print(f"❌ Error al leer el archivo: {e}")