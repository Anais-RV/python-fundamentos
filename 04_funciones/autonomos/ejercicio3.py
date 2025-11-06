# EJERCICIO AUTÓNOMO 3: Formatear gato
# Enunciado: `formatear_gato(nombre, edad)` -> string con f-string

# TODO 1: Crear funcion 'formatear_gato(nombre, edad)
def formatear_gato(nombre, edad):

    # TODO 1.1: Verificar si edad es un número usando try/except
    try:
        # TODO 1.2: Intentar convertir edad a int
        edad = int(edad)

        # TODO 1.3: Devuelve un string con formato de texto f-string
        return f"\nSu gato se llama {nombre} y tiene {edad} años."

    # TODO 1.4: Mensaje de error si edad no es un número
    except ValueError:
        print("\nERROR ❌. Edad debe ser un número")

# TODO 2: Crear función principal
def main():

    # TODO 2.1: Imprimir título del ejercicio
    print("--- Formatear Gato ---")
    
    # TODO 2.2: Pedir datos al usuario
    nombre = input("\nIntroduce el nombre de su gato --> ")
    edad = input("Introduce la edad de su gato --> ")

    # TODO 2.3: Imprimir función con los valores añadidos
    print(formatear_gato(nombre, edad)) 

# TODO 3: Punto de entrada del programa
if __name__ == "__main__":
       main()

# EJEMPLO:
# --- Formatear Gato ---
# 
# Introduce el nombre de su gato --> Pequeflus
# Introduce la edad de su gato --> 10
#
# Su gato se llama Pequeflus y tiene 10 años.
# ---------------------------------------------
# Éxito ✅