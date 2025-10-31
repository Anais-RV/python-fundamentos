print("Indica peso (KG - solo numero) de gato 1:")
kg_gato_1_input = input()
kg_gato_1 = int(kg_gato_1_input)

if not kg_gato_1:
  print("Dato no válido")

print("Indica peso (KG - solo numero) de gato 2:")
kg_gato_2_input = input()
kg_gato_2 = int(kg_gato_2_input)

if not kg_gato_2:
  print("Dato no válido")

print("Indica peso (KG - solo numero) de gato 3:")
kg_gato_3_input = input()
kg_gato_3 = int(kg_gato_3_input)

if not kg_gato_3:
  print("Dato no válido")

avg_kg = (kg_gato_1 + kg_gato_2 + kg_gato_3) / 3
print(round(avg_kg, 2))