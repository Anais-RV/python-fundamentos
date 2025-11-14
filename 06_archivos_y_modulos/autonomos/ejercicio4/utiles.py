# utiles.py
# Módulo donde se almacena funciones útiles para leer y escribir archivos

# TODO 1: Función que lee el contenido del archivo y las líneas de texto que contiene
def leer_lineas(ruta):
    try:
        print("Leyendo archivo... \n")
        with open(ruta, 'r', encoding="utf-8") as archivo:

            contenido = archivo.read()
            print(contenido)

        print("\nContando número de líneas:")
        with open(ruta, 'r', encoding="utf-8") as archivo:

            lineas = archivo.readlines()
            print(len(lineas) - 1)

        print(f"Archivo {ruta} corregido con éxito ✅")

    except FileNotFoundError:
        print("❌ Archivo no encontrado.\n")
    except Exception as e:
        print(f"\n❌ Error al leer el archivo: {e}")

# TODO 2: Función para guardar las líneas a un archivo específico
def guardar_lineas(ruta, lineas):
    try:
        print("Escribiendo archivo...\n")
        with open(ruta, 'w', encoding="utf-8") as archivo:

            for linea in lineas:
                archivo.write(f"\n{linea}")
        
        print(f"Archivo {ruta} creado con éxito ✅")
    except FileNotFoundError:
        print("❌ Archivo no encontrado.\n")
    except Exception as e:
        print(f"\n❌ Error al escribir el archivo: {e}")
