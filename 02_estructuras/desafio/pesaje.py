# DESAFIO: Bigotes Felices (pesaje)
# Enunciado: Pide el peso de tres gatos y calcula el promedio.
# Valida entradas numéricas. 

gato1 = input("Introduce el peso del primer gato: ")
gato2 = input("Introduce el peso del segundo gato: ")
gato3 = input("Introduce el peso del tercer gato: ")

gato1 = int(gato1)
gato2 = int(gato2)
gato3 = int(gato3)

promedio = (gato1 + gato2 + gato3) / 3

print(f"Pesaje de los gatos: ")
print(f"Gato nº1: {gato1} kg")
print(f"Gato nº2: {gato2} kg")
print(f"Gato nº3: {gato3} kg")
print(f"Calculo promedio de los 3 gatos: {promedio}")

# Primer test: introducir '10', '20' y '30' respectivamente cuando le pida el programa
# Resultado al ejecutar 'python pesaje.py':
# ---------------------------------------
# Introduce el peso del primer gato: 10
# Introduce el peso del segundo gato: 20
# Introduce el peso del tercer gato: 30
# Pesaje de los gatos:
# Gato nº1: 10 kg
# Gato nº2: 20 kg
# Gato nº3: 30 kg
# Calculo promedio de los 3 gatos: 20.0 
# ---------------------------------------
# Éxito ✅ 