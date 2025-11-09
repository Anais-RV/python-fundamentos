import sol_4_utiles

# Guardar líneas en un archivo
lineas = ["Gato", "Perro", "Conejo"]
sol_4_utiles.guardar_lineas("animales.txt", lineas)

# Leer las líneas del archivo
resultado = sol_4_utiles.leer_lineas("animales.txt")
print(resultado)