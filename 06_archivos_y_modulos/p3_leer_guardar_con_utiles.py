import utiles 

ruta = "datos.txt"
lineas_a_guardar = ["Linea 1", "Linea 2", "Linea 3"]

# Guardar 

utiles.guardar_lineas(ruta, lineas_a_guardar)
print("\n-- Líneas guardadas")

# Leer 
lineas_leidas = utiles.leer_lineas(ruta)
print("-- Lineas leidas desde archivo")
for linea in lineas_leidas:
    print("\t" + linea)

