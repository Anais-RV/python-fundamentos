def area_rectangulo(a, b):
    if not isinstance(a, float) or not isinstance(b, float):
        raise TypeError("a y b deben ser números")

    if a <= 0 or b <= 0:
        raise ValueError("a y b deben ser mayores que cero")

    return a * b

print("Dame BASE (A - m2):")
user_input_a = input()
user_a = float(user_input_a)

print("Dame ALTURA(B - m2):")
user_input_b = input()
user_b = float(user_input_b)

area = area_rectangulo(user_a, user_b)
print(f"El área total es de: {area} m2")