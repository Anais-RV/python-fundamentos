# app.py
# Script para utilizar las funciones de 'utiles.py'

# TODO 1: Importar funciones de utiles
from utiles import leer_lineas, guardar_lineas

# TODO 2: Imprimir título de app.py
print("--- APP ---")

# Lista de lineas de comida
lista = [
    "Cachopo",
    "Escalopines",
    "Solomillo",
    "Merluza",
    "Zanahoria"
]

# Archivo (sin nombre ni prefijo)
archivoTXT = ""

# Funcion que guarda las líneas
guardar_lineas(archivoTXT, lista)

# Funcion que lee las líneas
leer_lineas(archivoTXT)

# RESULTADO:
# --- APP ---
# Escribiendo archivo...
# 
# ❌ Archivo no encontrado.
# 
# Leyendo archivo...
#
# ❌ Archivo no encontrado.
