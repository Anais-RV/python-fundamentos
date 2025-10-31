print("Dame un número:")
num_input = input()

try:
  int(num_input)
  print("Ejercicio completado")
except:
  print("Entrada inválida")