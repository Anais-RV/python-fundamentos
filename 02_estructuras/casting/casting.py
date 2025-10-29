# EJERCICIO GUIADO 2: CASTING Y VALICADIÓN
# Paso 1: Crea `casting.py` que pida un número con `input`.
# Paso 2: Convierte a `int` dentro de `try/except`.
# Paso 3: Si falla, imprime `Entrada inválida`.

casting = input("Introduce un número --> ")

try:
    casting = int(casting)
    print(casting)
except ValueError:
    print(f"Entrada inválida")

# Segundo test: introducir python cuando lo pidan --> Sale error ❌
# Motivo: ValueError: invalid literal for int() with base 10: 'python'