from collections import Counter
import csv

# Archivo de entrada y salida
entrada = "visitas.log"
salida = "resumen_visitas.csv"

# Contador de visitas por día
conteo = Counter()

# Leer el archivo línea por línea
with open(entrada, "r", encoding="utf-8") as f:
    for linea in f:
        # Tomamos la fecha (primer campo antes del espacio)
        fecha = linea.split()[0]
        conteo[fecha] += 1

# Guardar resumen en CSV
with open(salida, "w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["Fecha", "Visitas"])
    for fecha, visitas in sorted(conteo.items()):
        escritor.writerow([fecha, visitas])

print("✅ Resumen guardado en 'resumen_visitas.csv'")
