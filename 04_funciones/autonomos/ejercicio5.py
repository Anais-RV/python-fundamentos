# EJERCICIO AUTÓNOMO 5: Leer edad
# Enunciado: `leer_edad()` pide una edad por `input()`, valida `ValueError` y retorna un entero o `None`.

# TODO 1: Crear funcion 'leer_edad()'
def leer_edad():
    # TODO 1.2: Verificar si el valor introducido es un número usando try/except
    try:
        # TODO 1.3: Pedir la edad del usuario
        edad = int(input("\nIntroduce tu edad --> "))

        # TODO 1.4: Retorna el número entero en formato de texto f-string
        return f"\nEdad: {edad} años \n"
    # TODO 1.5: Mostrar 'None' si el valor introducido no es un número
    except ValueError:
        return None

# TODO 2: Crear función principal    
def main():
    # TODO 2.1: Imprimir titulo del ejercicio
    print("--- Leer edad ---")
    # TODO 2.2: Imprimir función con el valor a pedir
    print(leer_edad())

# TODO 3: Punto de entrada del programa
if __name__ == "__main__":
    main()

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