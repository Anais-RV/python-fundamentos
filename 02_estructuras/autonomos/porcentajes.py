# EJERCICIO AUTÓNOMO 4: PORCENTAJES
# Enunciado: calcula el 15% de una cantidad.

# Variable num al pedir un número entero
num = input("Introduce un número: ")

# Efecto try/except por si deja convertir la variable num a entero
try: 
    # Convertir string num a int num
    num = int(num)

    # Variable porcentaje a calcular el 15% del numero dado
    porcentaje = 0.15

    # Variable resultado para calcular el resultado del 15% del numero dado
    resultado = num * porcentaje

    # Imprimir resultado del ejercicio
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