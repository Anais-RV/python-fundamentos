def sumar(nums):
    if not isinstance(nums, list):
        raise TypeError("nums debe ser una lista")
    
    for n in nums:
        if not isinstance(n, (int, float)):
            raise ValueError("Todos los elementos deben ser números")
    
    return sum(nums)

def sumar_user():
    nums = []

    while True:
        print("Introduce un número (o FIN para terminar):")
        entrada = input()

        if entrada.lower() == "fin":
            break
        
        try:
            valor = float(entrada)
            nums.append(valor)
        except ValueError:
            print("Por favor introduce un número válido o FIN.")

    total = sumar(nums)
    print(f"El total es: {total}")
    return total

sumar_user()