def reto1():
    while (comando := input("Comando: ").strip().lower()) != "salir":
        partes = comando.split()

        if len(partes) != 3:
            print("Comando no válido")
            continue

        operacion, x_str, y_str = partes

        try:
            x, y = float(x_str), float(y_str)
        except ValueError:
            print("Argumentos no válidos")
            continue

        if operacion == "sumar":
            print(f"{x} + {y} = {x + y}")
        elif operacion == "restar":
            print(f"{x} - {y} = {x - y}")
        elif operacion == "multiplicar":
            print(f"{x} * {y} = {x * y}")
        elif operacion == "dividir":
            if y == 0:
                print("No se puede dividir por cero")
            else:
                print(f"{x} / {y} = {x / y}")
        else:
            print("Comando no válido")

    print("Hasta pronto")