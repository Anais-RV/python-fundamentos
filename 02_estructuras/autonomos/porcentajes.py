# EJERCICIO AUTÓNOMO 4: PORCENTAJES
# Enunciado: calcula el 15% de una cantidad.

num = input("Introduce un número: ")

num = int(num)

porcentaje = 0.15

resultado = num * porcentaje

print(f"15% de {num} --> {resultado}")

# Segundo test: introducir 'Hola' como num cuando lo pide el programa
# Resultado al ejecutar 'python porcentajes.py':
# --------------------------
# ERROR ❌
# --------------------------
# Motivo: ValueError: invalid literal for int() with base 10: 'Hola'