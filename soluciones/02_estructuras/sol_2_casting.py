txt = input("Número: ")
try:
    n = int(txt)
    print(n)
except ValueError:
    print("Entrada inválida")
