print("Indica el número de gatos:")
cats_input = input()

try:
  cats = int(cats_input)
except ValueError:
  print("Por favor introduce un número válido.")

turno_A = []
turno_B = []

for i in range(1, cats + 1):
    if i % 2 == 0:
        turno_B.append(f"Gato {i}")
    else:
        turno_A.append(f"Gato {i}")

print("Turno A:", turno_A)
print("Turno B:", turno_B)