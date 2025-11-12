# app.py
# Script para utilizar las funciones de 'utiles.py'

# TODO 1: Importar funciones de utiles
from utiles import leer_lineas, guardar_lineas

# TODO 2: Imprimir título de app.py
print("--- APP ---")

# TODO 3: Ejemplos básicos

# Nº1 Gestión de tareas

tareas = [
    "Despertarme a las 8:30",
    "Estudiar hasta las 14:30",
    "Jugar Pokemon hasta las 21:30",
    "Dormir hasta el día siguiente"
]

tareaTxt = "tarea.txt"

guardar_lineas(tareaTxt, tareas)

leer_lineas()