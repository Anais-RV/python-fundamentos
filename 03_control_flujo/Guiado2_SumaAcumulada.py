print("Acumulador de números")

acumulador = 0.0 

while True:
    entrada = input("Dame un número o escribe FIN para salir: ")

    if entrada.lower() == "fin":
        break

    try:
        numero = float(entrada)
        acumulador += numero
    except ValueError:
        print("valor incorrecto")

print(f"el total es: {acumulador}")
