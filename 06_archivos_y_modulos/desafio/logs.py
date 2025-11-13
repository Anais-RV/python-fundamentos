# funciones.py
# Módulo donde se almacena funciones útiles para guardar y leer archivos LOG
import os

# Función que almacena el contenido del archivo ruta
def guardar_archivo(ruta, lineas):
    try:
        print(f"\nEscribiendo archivo {ruta}...")

        with open(ruta, 'w', encoding="utf-8") as archivo:

            for i, linea in enumerate(lineas, 1):
                archivo.write(f"\n{i}º log:\n")
                for clave, valor in linea.items():
                    line = f"| {clave} - {valor} |"
                    archivo.write(line)
            
        print(f"Archivo {ruta} creado y escrito con éxito ✅")
     
    except FileNotFoundError:
        print("❌ El archivo no existe")
    except Exception as e:
        print(f"❌ Error al escribir el archivo: {e}")

# Función que lee el contenido ruta
def resumen_archivo(ruta):

    try:
        print(f"\nLeyendo y analizando archivo {ruta}...")
        with open(ruta, "r", encoding="utf-8") as archivo:

            contenido = archivo.read()
            print(contenido)

        with open(ruta, "r", encoding="utf-8") as archivo:

            lineas = archivo.readlines()
            print(f"\nNúmero de líneas: {len(lineas)-1}")
    
        print(f"Archivo {ruta} leído correctamente ✅")
    except FileNotFoundError:
        print("❌ El archivo no existe.")
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")

# Funcion de número de visitas por día
def visita_por_dia(ruta):
    print("\n-- Visitas por día --")
    # Dict vacío para almacenar fechas de logs
    visitasXdia = {}

    try:
        print("--- Analizando ---")
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                # Verificar si la linea recorrida tiene más de 10 caracteres
                if len(linea) >= 10:
                    # Extraer la fecha (| fecha - "2024-10-12" 18:21:51 | recogemos desde el índice 10 hasta el 20 que recoge la fecha)
                    fecha = linea[10:20] # Slicing para extraer la fecha

                    # Contamos la fecha para ese día
                    if fecha in visitasXdia:
                        visitasXdia[fecha] += 1
                    else:
                        visitasXdia[fecha] = 1

        print("Ánalisis completo. ✅")

        print("\nRESUMEN:")
        # Total de visitas de x días
        total_visitas = 0
        # Recorremos la lista de x fechas que se almacenaron en visitasXdia
        for fecha in visitasXdia:
            visitas = visitasXdia[fecha]
            total_visitas += visitas
            if visitas == 1:
                print(f"Fecha: {fecha} | {visitas} visita")
            else:
                print(f"Fecha: {fecha} | {visitas} visitas")
        # Resumen del total de visitas en x días
        print(f"Total de visitas: {total_visitas} visitas en {len(visitasXdia)} días.")

        
    except FileNotFoundError:
        print("❌ No se encontró el archivo especificado")
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")