print("¿Cuántos años tienes? (número)")
age_input = input()
age = int(age_input)

if not isinstance(age, int):
  print("Edad no válida.")
  exit()

print("¿Cuál es tu lugar favorito? (ciudad)")
city_input = input()
city = str(city_input)

if not isinstance(city, str):
  print("Ciudad no válida.")
  exit()

print("Dime tu color favorito:")
color_input = input()
color = str(color_input)

if not isinstance(color, str):
  print("color no válido.")
  exit()

print(f"Usuario actual tiene {age} años.")
print(f"Lugar favorito de usuario actual: {city}")
print(f"Color favorito de usuario actual: {color}")