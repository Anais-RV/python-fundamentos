# 1
with open("michis.csv", "w", enconding="utf-8") as archivo:
    archivo.write("Nombre,Edad\n")
    archivo.write("Michi, 2\n")
    archivo.write("Michifurri, 5\n")
    archivo.wirte("Furrimichi 12\n")
    
# 2 
def leer_lineas(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return archivo.areadlines()

def guardar_lineas(ruta, lineas):
    with open(ruta, "w", enconding="utf-8") as archivo:
        for linea in lineas:
            archivo.write(linea + "\n")
            
# 3
import os
import utiles

ruta = input("Ruta archivo: ")
if not os.path.exists(ruta):
    print("La ruta no es correcta.")
else:
    try:
        lineas = utiles.leer_lineas(ruta)
        print("Contenido del arhcivo: ")
        for i, linea in enumerate(lineas, 1):
            print(f"{i}. {linea.strip()}")
    except FileNotFound:
        print("Lo siento compi no se pudo abrir el archivo")