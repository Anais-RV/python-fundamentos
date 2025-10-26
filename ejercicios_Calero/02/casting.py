entrada = input("Introduce un número entero: ").strip()
try:
    numero = int(entrada)
    print(f"Número válido: {numero}")
except ValueError:
    print("Entrada no válida")