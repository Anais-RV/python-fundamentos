# EJERCICIO GUIADO 1: Clasificador simple
# Enunciado: Pide un número y clasifícalo como negativo, cero o positivo. Valida `ValueError`.

# TODO 0: Imprimir título del programa y su descripción
print("---- Clasificador cimple ----")
print("Pide un número y clasifícalo como negativo, cero o positivo.\n")

# TODO 1: Pedir número al usuario
num = input("Escribe un número --> ")

# TODO 2: Evaluar si es un número usando try/except
try:
    # TODO 3: Intentar convertir num a float
    num = float(num)

    # TODO 4: clasificar num usando if/elif/else
    if num < 0:
        print("Negativo")
    elif num == 0:
        print("Cero")
    else:
        print("Positivo")

# TODO 5: Mensaje de error si num no es un número
except ValueError:
    print(f"ERROR ❌. El número introducido no es un número.")

# Perfecto! Ahora ya se tiene un clasificador de números interactivo.
# Vamos a hacer pruebas:
# -----------------------------------------------------------------
# Nº1
# Escribe un número --> 10
# Positivo
# -----------------------------------------------------------------
# Nº2
# Escribe un número --> -25
# Negativo
# -----------------------------------------------------------------
# Nº3
# Escribe un número --> 0
# Cero
# -----------------------------------------------------------------
# Nº4
# Escribe un número --> pepe
# ERROR ❌. El número introducido no es un número.
# -----------------------------------------------------------------