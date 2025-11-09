numero_input = input("Imprime un número aquí: ")

try:
    numero = int(numero_input)
    print(f"Has imprimido el número: {numero}")

except ValueError:
    print("Entrada inválida")
