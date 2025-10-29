def main():
    # Pedimos el nombre del gato
    nombre = input("Introduce el nombre del gato: ")

    # Pedimos la edad
    edad_input = input("Introduce la edad del gato: ")

    try:
        # Intentamos convertir la edad a número
        edad = float(edad_input)
        print(f"Gato: {nombre} (edad: {edad})")
    except ValueError:
        # Si la conversión falla, mostramos un mensaje
        print("Edad inválida")

if __name__ == "__main__":
    main()