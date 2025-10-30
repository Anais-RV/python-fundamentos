# DESAFIO: Bigotes Felices (pesaje)
# Enunciado: Pide el peso de tres gatos y calcula el promedio.
# Valida entradas numéricas. 

# Variable gato1 al pedir al usuario el peso del 1º gato
gato1 = input("Introduce el peso del primer gato: ")
# Variable gato2 al pedir al usuario el peso del 2º gato
gato2 = input("Introduce el peso del segundo gato: ")
# Variable gato3 al pedir al usuario el peso del 3º gato
gato3 = input("Introduce el peso del tercer gato: ")

# Try/except para verificar si los datos introducidos son números enteros
try: 
    # Intentamos convertir gato1 en número entero
    gato1 = int(gato1)
    # Intentamos convertir gato2 en número entero
    gato2 = int(gato2)
    # Intentamos convertir gato3 en número entero
    gato3 = int(gato3)

    # Variable promedio para calcular el peso promedio de los 3 gatos
    promedio = (gato1 + gato2 + gato3) / 3

    print(f"Pesaje de los gatos: ")
    print(f"Gato nº1: {gato1} kg")
    print(f"Gato nº2: {gato2} kg")
    print(f"Gato nº3: {gato3} kg")
    print(f"Calculo promedio de los 3 gatos: {promedio}")

except ValueError:
    print(f"Error al introducir los datos. Por favor, vuelva a iniciar el pesaje.")

# Tercer test: introducir 'hola', 'que' y 'cachopo' respectivamente cuando le pida el programa
# Resultado al ejecutar 'python pesaje.py':
# ---------------------------------------
# Introduce el peso del primer gato: hola
# Introduce el peso del segundo gato: que 
# Introduce el peso del tercer gato: cachopo
# Error al introducir los datos. Por favor, vuelva a iniciar el pesaje.
# ---------------------------------------
# Éxito ✅ 