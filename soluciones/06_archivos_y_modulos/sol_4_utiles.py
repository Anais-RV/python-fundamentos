def leer_lineas(ruta):
    """
    Lee todas las líneas de un archivo de texto y las devuelve como una lista.
    Cada línea se devuelve sin el salto de línea final.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return [linea.strip() for linea in f.readlines()]
    except FileNotFoundError:
        print(f"⚠️ El archivo '{ruta}' no existe.")
        return []
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return []


def guardar_lineas(ruta, lineas):
    """
    Guarda una lista de cadenas en un archivo de texto,
    escribiendo una línea por cada elemento de la lista.
    """
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            for linea in lineas:
                f.write(str(linea) + "\n")
        print(f"✅ Archivo '{ruta}' guardado correctamente.")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")