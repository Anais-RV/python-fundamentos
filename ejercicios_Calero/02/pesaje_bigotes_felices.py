def leer_peso(gato_num):
    entrada = input(f"Peso del michi {gato_num} (kg): ").strip().replace(",", ".")
    try:
        peso = float(entrada)
        return peso
    except ValueError:
        print("¡Pon un valor válido para el peso del michi!")
        return None
    
pesos = []
for i in range (1, 4):
    peso_valido = None
    while peso_valido is None:
        peso_valido = leer_peso(i)
    pesos.append(peso_valido)
    
promedio = round(sum(pesos) / len(pesos), 2)
print(f"Peso promedio de los gatos: {promedio} kg")