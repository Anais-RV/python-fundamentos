pesos = [3.5, 4.2, 2.8, 5.0, 4.7, 3.9]


ordenados = sorted(enumerate(pesos), key=lambda x: x[1], reverse=True)

print("Top 3 gatos más pesados:")
for i, peso in ordenados[:3]:
    print(f"Gato #{i+1}: {peso} kg")