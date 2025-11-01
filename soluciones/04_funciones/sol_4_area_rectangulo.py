def area_rectangulo(a: float, b: float) -> float:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a y b deben ser números")
    if a <= 0 or b <= 0:
        raise ValueError("a y b deben ser mayores que 0")
    return a * b

if __name__ == "__main__":
    print(area_rectangulo(7, 6))
    print(area_rectangulo(-2, 5))
    print(area_rectangulo(8, "4"))