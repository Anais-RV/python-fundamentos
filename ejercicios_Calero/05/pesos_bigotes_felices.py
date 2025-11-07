pesos_michis = [3.5, 33.2, 4.0, 6.6, 8.4, 7.6, 1.2]
pesos_ordenados = sorted(pesos_michis, reverse=True)
top3 = pesos_ordenados[:3]
print("Los tres michis mas gordacos son: ")
for i, peso in enumerate(top3, 1):
    print(f"{i}. {peso} kg")