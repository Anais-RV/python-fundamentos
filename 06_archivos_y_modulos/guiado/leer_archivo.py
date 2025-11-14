# EJERCICIO GUIADO 2: Leer archivo
# ENUNCIADO: Lee `escribir.txt` e imprime las líneas numeradas.

ARCHIVOTXT = 'escribir.txt'

try:
    with open(ARCHIVOTXT, 'r') as archivo:
        lineas = archivo.readlines()

        print("\nContenido del archivo: ")

        for numero, linea in enumerate(lineas, 1):
            # Usamos .rstrip() para eliminar el salto de línea al final
            print(f"{numero}. {linea.rstrip()}")
        
        print(f"\n--- Información del archivo ---")
        print(f"Total de líneas: {len(lineas)}")

except FileNotFoundError:
    print("❌ No se encontró el archivo")