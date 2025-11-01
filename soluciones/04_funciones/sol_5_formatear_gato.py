def formatear_gato(nombre: str, edad: int) -> str:
    if not isinstance(nombre, str):
        raise TypeError("nombre debe ser una cadena")
    if not isinstance(edad, int):
        raise TypeError("edad debe ser un número entero")
    return f"El gato se llama {nombre} y tiene {edad} años."

if __name__ == "__main__":
    print(formatear_gato("Garfield", 6))
    print(formatear_gato(6, 6))
    print(formatear_gato("Garfield", 6.7))