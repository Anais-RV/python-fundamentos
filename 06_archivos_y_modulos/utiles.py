
def leer_lineas(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return [linea.rstrip('\n') for linea in archivo]
    except FileNotFoundError:
        print(f"El archivo '{ruta}' no existe.")
        return []


def guardar_lineas(ruta, lineas):
    with open(ruta, 'w', encoding='utf-8') as archivo:
        for linea in lineas:
            archivo.write(f"{linea}\n")
