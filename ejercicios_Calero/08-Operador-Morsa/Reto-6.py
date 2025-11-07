from collections import Counter

def reto6():
    archivo_entrada = input("Archivo de logs: ").strip()
    archivo_salida = "resumen.txt"
    contador_tipo = Counter()
    contador_fecha = Counter()

    try:
        with open(archivo_entrada, "r", encoding="utf-8") as f:
            while (linea := f.readline()):
                if (partes := linea.strip().split()) and len(partes) >= 2:
                    fecha, tipo = partes[0], partes[1]
                    contador_fecha[fecha] += 1
                    contador_tipo[tipo] += 1

        with open(archivo_salida, "w", encoding="utf-8") as out:
            out.write("Conteo por tipo:\n")
            for tipo, cantidad in contador_tipo.items():
                out.write(f"{tipo}: {cantidad}\n")

            out.write("\nConteo por fecha:\n")
            for fecha, cantidad in contador_fecha.items():
                out.write(f"{fecha}: {cantidad}\n")

        print("Resumen guardado en resumen.txt")

    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")