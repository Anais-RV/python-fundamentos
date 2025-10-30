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

    # Volver a declarar variable promedio para redondear a 3 decimales con la funcion round()
    promedio = round(promedio, 3)

    # Imprimir titulo del pesaje de los gatos
    print(f"Pesaje de los gatos: ")
    # Imprimir peso del gato nº1
    print(f"Gato nº1: {gato1} kg")
    # Imprimir peso del gato nº2
    print(f"Gato nº2: {gato2} kg")
    # Imprimir peso del gato nº3
    print(f"Gato nº3: {gato3} kg")
    # Imprimir peso promedio de los 3 gatos
    print(f"Calculo promedio de los 3 gatos: {promedio}")

# Metodo except por si el dato introducido no es un número entero
except ValueError:
    # Si uno de los 3 valores pedidos no es un número entero mostrará este mensaje de error
    print(f"Error al introducir los datos. Por favor, vuelva a iniciar el pesaje.")

# Quinto test: introducir '12', '34' y '40' respectivamente cuando le pida el programa
# Resultado al ejecutar 'python pesaje.py':
# ---------------------------------------
# Introduce el peso del primer gato: 12
# Introduce el peso del segundo gato: 34
# Introduce el peso del tercer gato: 40
# Pesaje de los gatos: 
# Gato nº1: 12 kg
# Gato nº2: 34 kg
# Gato nº3: 40 kg
# Calculo promedio de los 3 gatos: 28.667
# ---------------------------------------
# Éxito ✅ 