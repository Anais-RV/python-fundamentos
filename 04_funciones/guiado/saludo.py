# Guiado 1: Función saludo
# Enunciado: Crea `def saludar(nombre):` que retorne `Hola, <nombre>`.

# TODO 0: Imprime el titulo de ejercicio
print("--- Función Saludo ---")
# TODO 1: Crearemos una función con 1 parámetro (nombre) para mostrar el saludo
def saludar(nombre):
    # TODO 2: Devuelve el saludo
    return f"Hola, {nombre}"

# TODO 2: Pide un nombre al usuario
nombre = input("\nIntroduce un nombre --> ")

# TODO 3: Punto de entrada del programa
if __name__ == "__main__":
    print(saludar(nombre))

# Resultado:
# --- Función Saludo ---
#
# Introduce un nombre --> Pedro
# Hola, Pedro
# -----------------------------
# Éxito ✅