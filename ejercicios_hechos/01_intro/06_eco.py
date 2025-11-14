print("Dime algo y haré eco:")
user_input = input()
message = str(user_input)

if isinstance(message, str):
  print(f"{message}")
else:
  print("Mensaje no válido")