def leer_lineas(ruta):
    print ("\nleyendo...")
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return [linea.rstrip('\n') for linea in archivo]
    except FileNotFoundError:
        print(f"El archivo '{ruta}' no existe")
        return []
    
    


print(leer_lineas("./datos.txt"))