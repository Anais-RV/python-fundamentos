entrada = input("Introduce un numero: ")

try:
    numero = float(entrada)
    print(f"Has introducido el numero {numero}")
except ValueError:
    print("Eso no parece un nuemero válido.")