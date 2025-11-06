# EJERCICIO AUTÓNOMO 3: Formatear gato
# Enunciado: `formatear_gato(nombre, edad)` -> string con f-string

def formatear_gato(nombre, edad):
    return f"Su gato se llama {nombre} y tiene {edad} años."

if __name__ == "__main__":
    print("--- Formatear Gato ---")

    try:
        nombre = str(input("\nIntroduce el nombre de su gato --> "))
        edad = int(input("Introduce la edad de su gato --> "))

        print(formatear_gato(nombre, edad))
    
    except ValueError:
        print("\nEntrada inválida ❌")

# EJEMPLO:
# --- Formatear Gato ---
# 
# Introduce el nombre de su gato --> Pequeflus
# Introduce la edad de su gato --> 10
# Su gato se llama Pequeflus y tiene 10 años.
# ---------------------------------------------
# Éxito ✅