with open("escribir.txt", "w", enconding="utf-8") as archivo: #el open("escribir.txt", "w" abre archivo en formato escritura (lo crea o lo sobrescribee)
    
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea\n")
    archivo.write("Tercera línea\n")