try:
    numero = float(input("¿Qué número eliges?: "))
    if numero > 0:
        print("¡El número es positivo!")
    elif numero < 0:
        print("¡El número es negativo!")
    elif numero == 0:
        print("¡El número es cero!")
except ValueError:
    print("¡Entrada no válida!")