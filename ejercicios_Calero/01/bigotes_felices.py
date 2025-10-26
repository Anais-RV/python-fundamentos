nombre = input("Nombre del michi: ").strip()
edad_input = input("Edad del michi: ").strip()

try:
    edad = float(edad_input)
    print(f"Gato: {nombre} (edad: {edad})")
except ValueError:
    print("Edad no válida")