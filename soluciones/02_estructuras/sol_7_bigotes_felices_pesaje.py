try:
    gato1_peso = float(input("Imprime el peso del primer gato aquí: "))
    gato2_peso = float(input("Imprime el peso del segundo gato aquí: "))
    gato3_peso = float(input("Imprime el peso del tercer gato aquí: "))
except ValueError:
    print("Entrada inválida")
else:
    promedio_de_pesos = (gato1_peso + gato2_peso + gato3_peso) / 3
    print(f"Aquí tienes el promedio: {promedio_de_pesos}")