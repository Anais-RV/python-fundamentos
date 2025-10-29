# EJERCICIO GUIADO 2: CASTING Y VALICADIÓN
# Paso 1: Crea `casting.py` que pida un número con `input`.
# Paso 2: Convierte a `int` dentro de `try/except`.
# Paso 3: Si falla, imprime `Entrada inválida`.

# Variable casting que pide un número con `input`
casting = input("Introduce un número --> ")

try:
    casting = int(casting)
    print(casting)
except ValueError:
    print(f"Entrada inválida")

# Tercer test: introducir python cuando lo pidan 
# Resultado impresión: Entrada inválida ✅