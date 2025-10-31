print("Introduce nombre gato:")
name_input = input()
name = str(name_input)

if not name:
  print("Nombre no válido")
  exit()

print("Introduce la edad del felino:")
age_input = input()
age = int(age_input)

if not isinstance(age, int):
  print("Edad no válida")

print("Añadido a la base de datos:")
print(f"Gato: {name} (edad: {age})")