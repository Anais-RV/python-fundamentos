# EJERCICIO GUIADO 2: Suma acumulada
# Enunciado: Suma números introducidos por el usuario hasta que escriba `fin`. Muestra el total. 

# TODO 0: Imprimir título del programa y su descripción
print("---- Suma acumulada ----")
print("Suma números introducidos por el usuario hasta que escriba 'fin'.\n")

# TODO 1: definir variable que cuente el total de numeros sumados empezando desde 0
total = 0

# TODO 2: iniciar bucle while que permite introducir tantos datos como quiera el usuario hasta escribir 'fin'
while True:
    # TODO 3: pedir un número al usuario
    num = input("Introduce un número (escribe 'fin' para terminar)--> ")

    # TODO 4: condicional 'if' si escribe 'fin' se acaba el programa y termina el bucle
    if (num == 'fin'):
        print("\nSe acabó!!")
        print("------------------------")
        break

    # TODO 5: condicional 'else' si no escribe 'fin' y siga funcionando el bucle
    else:
        # TODO 6: Evaluar el valor introducido usando try/except
        try:
            # TODO 7: Intentar convetir num a float
            num = float(num)
            # TODO 8: Acumular total con el número introducido
            total = total + num
            # TODO 9: Imprimir numero introducido y el total acumulado
            print(f"Número: {num} | Suma total: {total}")
        # TODO 10: Mostrar mensaje de error si el valor introducido no es un número
        except ValueError:
            print(f"El valor introducido ({num}) no es un número.")
            print("Por favor, introduce un número válido o 'fin' para terminar\n")
            continue

# TODO 11: Imprimir el total acumulado una vez salido del bucle while
print(f"Total acumulado: {total}")

# Prueba del programa:
# ---- Suma acumulada ----
# Suma números introducidos por el usuario hasta que escriba 'fin'.
#
# Introduce un número (escribe 'fin' para terminar)--> 4
# Número: 4.0 | Suma total: 4.0
# Introduce un número (escribe 'fin' para terminar)--> 2
# Número: 2.0 | Suma total: 6.0
# Introduce un número (escribe 'fin' para terminar)--> 9
# Número: 9.0 | Suma total: 15.0
# Introduce un número (escribe 'fin' para terminar)--> 6
# Número: 6.0 | Suma total: 21.0
# Introduce un número (escribe 'fin' para terminar)--> yo
# El valor introducido (yo) no es un número.
# Por favor, introduce un número válido o 'fin' para terminar
#
# Introduce un número (escribe 'fin' para terminar)--> fin
#
# Se acabó!!
# ------------------------
# Total acumulado: 21.0
#
# Resultado: éxito ✅