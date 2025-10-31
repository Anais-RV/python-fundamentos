print("Dame un número")
input_num = input()
float_num = float(input_num)

if isinstance(float_num, float):
  print(f"{float_num}")
else:
  print("Número no válido")

