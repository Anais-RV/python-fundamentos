# DESAFIO: Bigotes Felices (pesaje)
# Enunciado: Pide el peso de tres gatos y calcula el promedio.
# Valida entradas numéricas. 

gato1 = input("Introduce el peso del primer gato: ")
gato2 = input("Introduce el peso del segundo gato: ")
gato3 = input("Introduce el peso del tercer gato: ")

try: 
    gato1 = int(gato1)
    gato2 = int(gato2)
    gato3 = int(gato3)

    promedio = (gato1 + gato2 + gato3) / 3

    print(f"Pesaje de los gatos: ")
    print(f"Gato nº1: {gato1} kg")
    print(f"Gato nº2: {gato2} kg")
    print(f"Gato nº3: {gato3} kg")
    print(f"Calculo promedio de los 3 gatos: {promedio}")

except ValueError:
    print(f"Error al introducir los datos. Por favor, vuelva a iniciar el pesaje.")

# Segundo test: introducir 'hola', 'que' y 'cachopo' respectivamente cuando le pida el programa
# Resultado al ejecutar 'python pesaje.py':
# ---------------------------------------
# Introduce el peso del primer gato: hola
# Introduce el peso del segundo gato: que 
# Introduce el peso del tercer gato: cachopo
# Traceback (most recent call last):
#   File "C:\Users\Propietario\Documents\Archivos\Repositorios\python-fundamentos\02_estructuras\desafio\pesaje.py", line 9, in <module>
#     gato1 = int(gato1)
# ValueError: invalid literal for int() with base 10: 'hola'
# ---------------------------------------
# ERROR ❌
# Motivo: ValueError 