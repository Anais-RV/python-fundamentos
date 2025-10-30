# EJERCICIO AUTÓNOMO 2: STRINGS
# Enunciado: une nombre y apellido con espacio y `title()`.

# Variables nombre y apellido
# nombre: pide al usuario un nombre
# apellido: pide al usuario un apellido
nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")

# Variable string
# string: devuelve una cadena de texto que une nombre y apellido con un espacio
string = f"{nombre} {apellido}"

# Variable title
# title: devuelve string que incluye la funcion title()
# title(): devuelve una cadena en la que el primer carácter de cada palabra está en mayúscula. 
# Como un encabezado o un título.
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
