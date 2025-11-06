# EJERCICIO AUTÓNOMO 5: Leer edad
# Enunciado: `leer_edad()` pide una edad por `input()`, valida `ValueError` y retorna un entero o `None`.

# TODO 1: Crear funcion 'leer_edad()'
def leer_edad():
    # TODO 2: Imprimir titulo del ejercicio
    print("--- Leer edad ---")
    # TODO 3: Verificar si el valor introducido es un número usando try/except
    try:
        # TODO 4: Pedir la edad del usuario
        edad = int(input("\nIntroduce tu edad --> "))

        # TODO 5: Retorna el número entero en formato de texto f-string
        return f"\nEdad: {edad} años \n"
    # TODO 6: Mostrar 'None' si el valor introducido no es un número
    except ValueError:
        return "None\n"

# TODO 7: Punto de entrada del programa
if __name__ == "__main__":
    # TODO 8: Imprimir función con el valor a pedir
    print(leer_edad())

# EJEMPLO 1:
# --- Leer edad ---
#
# Introduce tu edad --> 23
#
# Edad: 23 años
#
# --------------------------
# EJEMPLO 2:
# --- Leer edad ---
#
# Introduce tu edad --> e
# None
#
#---------------------------
# Éxito ✅