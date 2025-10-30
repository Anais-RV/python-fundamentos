# EJERCICIO AUTÓNOMO 4: PORCENTAJES
# Enunciado: calcula el 15% de una cantidad.

num = input("Introduce un número: ")

try: 
    num = int(num)

    porcentaje = 0.15

    resultado = num * porcentaje

    print(f"15% de {num} --> {resultado}")

except ValueError:
    print("Valor incorrecto. Por favor reinicie el programa.")

# Tercer test: introducir 'Hola' como num cuando lo pide el programa
# Resultado al ejecutar 'python porcentajes.py':
# --------------------------
# Introduce un número: Hola
# Valor incorrecto. Por favor reinicie el programa.
# --------------------------
# Éxito ✅