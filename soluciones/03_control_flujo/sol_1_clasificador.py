txt = input("Número: ")
try:
    n = int(txt)
    if n > 0:
        print("positivo")
    elif n == 0:
        print("cero")
    else:
        print("negativo")
except ValueError:
    print("Entrada inválida")
