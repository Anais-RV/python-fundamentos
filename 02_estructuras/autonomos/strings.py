# EJERCICIO AUTÓNOMO 2: STRINGS
# Enunciado: une nombre y apellido con espacio y `title()`.

# Variables nombre y apellido
# nombre: pide al usuario un nombre
# apellido: pide al usuario un apellido
nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")

string = f"{nombre} {apellido}"

title = string.title()

print(title)

# Primer test: ejecutamos 'python strings.py'
# Cuando pida el programa pondremos 
# como nombre 'pepe' 
# y como apellido 'viyuela'
# Resultado esperado:
# Escribe tu nombre: pepe
# Escribe tu apellido: viyuela
# Pepe Viyuela
# Realizado con éxito ✅
