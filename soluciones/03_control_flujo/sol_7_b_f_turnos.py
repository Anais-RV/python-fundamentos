num_gatos = int(input("¿Cuántos gatos hay? "))

turno_A = []
turno_B = []

for i in range(1, num_gatos + 1):
    if i % 2 == 0:
        turno_B.append(f"Gato {i}")
    else:
        turno_A.append(f"Gato {i}")

print("\nTurno A:", turno_A)
print("Turno B:", turno_B)