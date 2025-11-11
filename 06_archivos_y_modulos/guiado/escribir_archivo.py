# EJERCICIO GUIADO 1: Escribir archivo
# ENUNCIADO: Crea `escribir.txt` con tres líneas.

ARCHIVOTXT = "escribir.txt"

try:
    with open(ARCHIVOTXT, "w") as archivo:

        # Escribir contenido en el archivo
        archivo.write("Hola, que tal?")
        archivo.write("\nMe encantan los cachopos")
        archivo.write("\nY también los chipis")

        # Cerrar el archivo
        archivo.close()
    print("\n✅ Creado y escrito el archivo correctamente.")
except Exception as e:
    print("\n❌ Error al escribir en el archivo txt: {e}")

try:
    with open(ARCHIVOTXT, "r") as archivo:
        
        print("\nLeyendo archivo...")

        # Leer el contenido del archivo
        contenido = archivo.read()

        # Imprimir el contenido
        print(contenido)

        # Cerrar el archivo
        archivo.close()

    print("\nArchivo leído correcto ✅")
except FileNotFoundError:
    print("❌ Archivo no encontrado")


