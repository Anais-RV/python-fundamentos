# EJERCICIO AUTÓNOMO 4: Contraseñas
# Enunciado: Pide contraseñas hasta que sea `gato123`.

# TODO 0: Imprimir título del programa
print("---- Contraseñas ----")

# TODO 1: Empezar bucle while que pida contraseñas hasta introducir 'gato123'
while True:
    # TODO 2: Pedir contraseña al usuario
    contrasena = input("\nIntroduce una contraseña ('gato123' para finalizar) --> ")
    # TODO 3: Si se introduce la contraseña especificada se acaba el bucle
    if contrasena == "gato123":
        print("Fin contraseñas!!!")
        break
    # TODO 4: Si no se introduce la contraseña especificada se guardará la contraseña introducida y seguirá pidiendo la contraseña
    else:
        print(f"Contraseña {contrasena} agregada.")
        continue

# RESULTADO:
# ---- Contraseñas ----
#
# Introduce una contraseña ('gato123' para finalizar) --> pepe
# Contraseña pepe agregada.
#
# Introduce una contraseña ('gato123' para finalizar) --> leoniko
# Contraseña leoniko agregada.
# 
# Introduce una contraseña ('gato123' para finalizar) --> gato123
# Fin contraseñas!!!