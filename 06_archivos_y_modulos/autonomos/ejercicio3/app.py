# app.py
# Script para utilizar las funciones de 'utiles.py'

# TODO 1: Importar funciones de utiles
from utiles import leer_lineas, guardar_lineas

# TODO 2: Imprimir título de app.py
print("--- APP ---")

# TODO 3: Ejemplo básico

# Gestión de tareas
print("\nEjemplo 1: Gestión de Tareas")

tareas = [
    "Despertarme a las 8:30",
    "Estudiar hasta las 14:30",
    "Jugar Pokemon hasta las 21:30",
    "Dormir hasta el día siguiente"
]

tareaTxt = "tarea.txt"

guardar_lineas(tareaTxt, tareas)

leer_lineas(tareaTxt)
