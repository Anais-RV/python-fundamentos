# EJERCICIO AUTÓNOMO 2: STRINGS
# Enunciado: une nombre y apellido con espacio y `title()`.

nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")

string = f"{nombre} {apellido}"

title = string.title()

print(title)