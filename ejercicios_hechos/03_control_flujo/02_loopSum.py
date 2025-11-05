total = 0

while True:
    print("Introduce un número (o FIN para terminar):")
    num_input = input()

    if num_input.lower() == "fin":
        break
    
    try:
        num = float(num_input)
        total += num
    except ValueError:
        print("Por favor introduce un número válido o FIN.")
        
print(f"El total es: {total}")
