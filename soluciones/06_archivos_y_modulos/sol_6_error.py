try:
    with open("archivo_inexistente.txt", "r", encoding="utf-8") as f:
        contenido = f.read()
        print(contenido)
except FileNotFoundError:
    print("⚠️ No se encontró el archivo 'archivo_inexistente.txt'.")
    print("💡 Asegúrate de que el archivo exista o revisa la ruta indicada.")