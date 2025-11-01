txt = input("Número: ")
try:
    x = int(txt)
    if x > 0:
        print("positivo")
    elif x == 0:
        print("cero")
    else:
        print("negativo")
except ValueError:
    print("Entrada inválida")
