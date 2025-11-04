# EJERCICIO AUTÓNOMO 3: Tablas de multiplicar
# Enunciado: Genera una tabla de multiplicar del 1 al 5 usando `for` anidados.

# TODO 0: Imprimir titulo del programa
print("---- TABLA DE MULTIPLICAR ----")

# TODO 1: Identificar el rango del 1 al 5 para las tablas de multiplicar
numeros = list(range(1, 6))
print(numeros)

# TODO 2: Empezar un bucle for que muestre los números de las tablas
for num1 in numeros:
    # TODO 3: Imprimir los numeros del 1 al 5 para que visualicen las tablas
    print(f"\nTabla del {num1}")
    # TODO 4: Añadir segundo bucle dentro del primero para que los numeros se crucen para las tablas
    for num2 in numeros:
        # TODO 5: Imprimir el calculo de cada tabla junto con el resultado
        print(f"{num1} x {num2} = {num1 * num2}")

# RESULTADO:
# ---- TABLA DE MULTIPLICAR ----
# [1, 2, 3, 4, 5]
#
# Tabla del 1
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5

# Tabla del 2
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 
# Tabla del 3
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
#
# Tabla del 4
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 
# Tabla del 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25