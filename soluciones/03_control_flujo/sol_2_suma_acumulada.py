total = 0
while True:
    entrada  = input("Introduce un número (o 'fin' para terminar): ")
    if entrada.lower() == "fin":
        break
    try:
        numero = float(entrada)
        total += numero
    except ValueError:
        print("Por favor, introduce un número válido o 'fin' para salir.")
print(f"La suma total es: {total}")
