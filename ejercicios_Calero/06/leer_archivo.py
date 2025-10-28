with open("escribir.txt", "r", encoding="utf-8") as archivo: #"r" modo lectura..
    for i, linea in enumerate(archivo, 1):
        print(f"{i}. {linea.strip()}")