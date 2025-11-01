def es_par(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("n debe ser un número entero")
    return n % 2 == 0

if __name__ == "__main__":
    print(es_par(7))
    print(es_par(9.8))