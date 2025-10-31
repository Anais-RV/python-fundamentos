print("¿Cómo te llamas?")
name = input()
str_name = str(name)

if not str_name:
  print("Nombre no váido.")
else:
  print(f"Hola, {name}")
