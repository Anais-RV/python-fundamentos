def reto3():
    archivo_entrada = input("Archivo a procesar: ").strip()
    archivo_salida = "datos_procesados.txt"

    procesadas = 0
    ignoradas = 0
    lineas_validas = []

    try:
        with open(archivo_entrada, "r", encoding="utf-8") as archivo:
            while (linea := archivo.readline()):
                if (linea_limpia := linea.strip()) and not linea_limpia.startswith("#") and len(linea_limpia) > 10:
                    lineas_validas.append(linea_limpia)
                    procesadas += 1
                else:
                    ignoradas += 1

        with open(archivo_salida, "w", encoding="utf-8") as salida:
            for linea in lineas_validas:
                salida.write(linea + "\n")

        print(f"Procesadas: {procesadas} líneas")
        print(f"Ignoradas: {ignoradas} líneas")
        print(f"Resultado guardado en: {archivo_salida}")

    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")