# utiles.py
# Módulo donde se almacena funciones útiles para leer y escribir archivos

import os

# TODO 1: Función que lee el contenido del archivo y las líneas de texto que contiene
def leer_lineas(ruta):

    if os.path.exists(ruta):
        print(f"\nSobrescribiendo archivo {ruta}...")

    print("\nLeyendo archivo... ")
    try:
            
        with open(ruta, 'r', encoding="utf-8") as archivo:

            contenido = archivo.read()
            print(contenido)

        print("\nContando número de líneas:")
        with open(ruta, 'r', encoding="utf-8") as archivo:

            lineas = archivo.readlines()
            print(len(lineas) - 1)

        print(f"Archivo {ruta} corregido con éxito ✅")

    # Agregar mensaje de error usando FileNotFoundError si no encuentra el archivo
    except FileNotFoundError:
        print("❌ Archivo no encontrado.\n")
    # Agregar mensaje de error usando FileExistsError si existe el archivo
    except FileExistsError:
        print(f"❌ El archivo {ruta} Ya existe ")
    # Agregar mensaje de error usando Exception si ha surgido otro tipo de error
    except Exception as e:
        print(f"\n❌ Error al leer el archivo: {e}")

# TODO 2: Función para guardar las líneas a un archivo específico
def guardar_lineas(ruta, lineas):

    print("\n Escribiendo archivo...")
    if os.path.exists(ruta):
        print(f"❌ El archivo {ruta} Ya existe ")
    
    else:
        try:
            
            with open(ruta, 'w', encoding="utf-8") as archivo:

                for linea in lineas:
                    archivo.write(f"\n{linea}")
        
            print(f"Archivo {ruta} creado con éxito ✅")
        # Agregar mensaje de error usando FileNotFoundError si no encuentra el archivo
        except FileNotFoundError:
            print("❌ Archivo no encontrado.\n")
        # Agregar mensaje de error usando FileExistsError si existe el archivo
        except FileExistsError:
            print(f"❌ El archivo {ruta} Ya existe ")
        # Agregar mensaje de error usando Exception si ha surgido otro tipo de error
        except Exception as e:
            print(f"\n❌ Error al escribir el archivo: {e}")
