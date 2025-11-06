# EJERCICIO AUTÓNOMO 1: Es par
# Enunciado: `es_par(n)` -> bool

# TODO 1: Crear la función 'def es_par(n)'
def es_par(n):
    # TODO 1.1: Verificar si el número es divisible por 2 y devuelva 0 (par) o no es divisible por 2 (impar)
    if n % 2 == 0:
        # TODO 1.2: Devuelve True si el número es par
        return True
    else:
        # TODO 1.3: Devuelve False si el número es impar
        return False

# TODO 2: Crear la funcion principal
def main():
    # TODO 2.1: Imprimir título del ejercicio
    print("--- Par o Impar ---")
    # TODO 2.2: Verificar si el valor introducido es un número usando try/except
    try:
        # TODO 2.3: Pedir un número al usuario
        num = int(input("\nEscribe un número (Resultado 'True' si es par; 'False' si es impar) --> "))
        # TODO 2.4: Imprimir la función con el número introducido
        print(es_par(num))
    # TODO 2.5: Mensaje de error si el valor introducido no es un número
    except ValueError:
        print("ERROR ❌. Debe introducir un número.")

    
# TODO 3: Punto de entrada del programa
if __name__ == "__main__":
    main()

# EJEMPLO:
# --- Par o Impar ---
# 
# Escribe un número (Resultado 'True' si es par; 'False' si es impar) --> 4
# True
# -------------------------------------------------------------------------
# Éxito ✅