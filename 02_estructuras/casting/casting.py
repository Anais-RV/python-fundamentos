# EJERCICIO GUIADO 2: CASTING Y VALICADIÓN
# Paso 1: Crea `casting.py` que pida un número con `input`.
# Paso 2: Convierte a `int` dentro de `try/except`.
# Paso 3: Si falla, imprime `Entrada inválida`.

# Variable casting que pide un número con `input`
casting = input("Introduce un número --> ")

try:
    # Intentamos convertir casting en int
    casting = int(casting)
    # Si lo convierte, imprime en consola
    print(casting)
except ValueError:
    # Salta mensaje de error 'ValueError' si el resultado no es un número entero
    print(f"Entrada inválida")

# Tercer test: introducir python cuando lo pidan 
# Resultado impresión: Entrada inválida ✅