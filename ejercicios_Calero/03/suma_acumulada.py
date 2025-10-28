suma_total = 0.0
while True:
    entrada = input("¿Número?")
    if entrada.lower() == "Acabose":
        break 
    
    try:
        numero = float(entrada)
        suma_total += numero
    except ValueError:
        print("Hay un error. Escribe un numero.")
        
print(f"La suma total es: {suma_total:.2f}")
