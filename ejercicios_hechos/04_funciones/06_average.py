def media(nums):
    if not isinstance(nums, list):
        raise TypeError("nums debe ser una lista")
    
    if len(nums) == 0:
        raise ValueError("La lista no puede estar vacía")
    
    for n in nums:
        if not isinstance(n, (int, float)):
            raise ValueError("Todos los elementos deben ser números")
    
    return sum(nums) / len(nums)


def media_user():
    nums = []

    while True:
        print("Introduce un número (o FIN para terminar):")
        user_input = input()

        if user_input.lower() == "fin":
            break
        
        try:
            num = float(user_input)
            nums.append(num)
        except ValueError:
            print("Por favor introduce un número válido o FIN.")

    if len(nums) == 0:
        print("No se introdujo ningún número, no se puede calcular la media.")
        return None

    result = media(nums)
    print(f"La media es: {round(result, 2)}")

media_user()
