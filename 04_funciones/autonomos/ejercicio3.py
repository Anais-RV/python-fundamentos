# EJERCICIO AUTÓNOMO 3: Formatear gato
# Enunciado: `formatear_gato(nombre, edad)` -> string con f-string

# TODO 1: Crear funcion 'formatear_gato(nombre, edad)
def formatear_gato(nombre, edad):
    # TODO 2: Imprimir título del ejercicio
    print("--- Formatear Gato ---")

    # TODO 3: Imprimir valores de los parámetros
    print(f"Nombre del gato: {nombre}")
    print(f"Edad del gato: {edad}")

    # TODO 4: Verificar si edad es un número usando try/except
    try:
        # TODO 5: Intentar convertir edad a int
        edad = int(edad)

        # TODO 6: Devuelve un string con formato de texto f-string
        return f"Su gato se llama {nombre} y tiene {edad} años."

    # TODO 7: Mensaje de error si edad no es un número
    except ValueError:
        print("\nERROR ❌. Edad debe ser un número")

# TODO 8: Agregar valores de los parámetros
nombre = "Pequeflus"
edad = 10

# TODO 9: Punto de entrada del programa
if __name__ == "__main__":
    # TODO 10: Imprimir función con los valores añadidos
    print(formatear_gato(nombre, edad))    

# EJEMPLO:
# --- Formatear Gato ---
# 
# Introduce el nombre de su gato --> Pequeflus
# Introduce la edad de su gato --> 10
# Su gato se llama Pequeflus y tiene 10 años.
# ---------------------------------------------
# Éxito ✅