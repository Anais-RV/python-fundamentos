total = 0.0
while True:
    s = input("n o fin: ")
    if s == "fin":
        break
    try:
        total += float(s)
    except ValueError:
        print("Entrada inválida")
print(total)
