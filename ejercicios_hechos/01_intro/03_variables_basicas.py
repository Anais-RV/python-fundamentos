print("¿Cómo te llamas?")
name = input()
str_name = str(name)

if not str_name:
  print("Dato no válido: Nombre")
  exit()

print("¿Dónde vives?")
city = input()
str_city = str(city)

if not str_city:
  print("Dato no válido: Ciudad")
  exit()

print(f"{str_name} vive en {str_city}")