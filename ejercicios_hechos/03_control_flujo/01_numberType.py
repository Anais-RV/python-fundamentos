print("Escribe un número:")
num_input = input()

try:
  num = int(num_input)
except ValueError:
  print("The value has wrong format")
except:
  print("Something else went wrong")

if num < 0:
  print(f"El número {num} es negativo")
elif num == 0:
  print(f"El número {num} es 0.")
elif num > 0:
  print(f"El número {num} es positivo.")