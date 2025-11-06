# EJERCICIO AUTÓNOMO 5: Leer edad
# Enunciado: `leer_edad()` pide una edad por `input()`, valida `ValueError` y retorna un entero o `None`.

def leer_edad():
    print("--- Leer edad ---")
    try:
        edad = int(input("\nIntroduce tu edad --> "))

        return f"\nEdad: {edad} años \n"
    except ValueError:
        return "None\n"

if __name__ == "__main__":
    print(leer_edad())
