def main():
    # Pedimos al usuario un número
    entrada = input("Introduce un número: ")
    
    try:
        # Intentamos convertir la entrada a float
        numero = float(entrada)
        print(f"Has introducido el número {numero}")
    
    except ValueError:
        # Si la conversión falla, mostramos un mensaje amable
        print("Parece que eso no es un número válido 😊. Inténtalo de nuevo.")

# Ejecutamos la función principal solo si el script se ejecuta directamente
if __name__ == "__main__":
    main() 