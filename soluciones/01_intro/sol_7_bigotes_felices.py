def main():
    
    nombre = input("Introduce el nombre del gato: ")
   
    edad_input = input("Introduce la edad del gato: ")

    try:
      
        edad = float(edad_input)
        print(f"Gato: {nombre} (edad: {edad})")
    except ValueError:
       
        print("Edad inválida")

if __name__ == "__main__":
    main()