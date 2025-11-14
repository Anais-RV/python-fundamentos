# Reto 1: Procesador interactivo de comandos
# Enunciado: Crea un programa que procese comandos hasta que el usuario escriba "salir".
#
# **Requisitos**:
# - Usa operador morsa en el bucle `while`
# - Comandos: `sumar x y`, `restar x y`, `multiplicar x y`, `dividir x y`
# - Valida que los números sean correctos
# - Muestra error si el comando no es válido 
#
# **Ejemplo de uso**:
# ```
# Comando: sumar 5 3
# ✅ 5 + 3 = 8
#
# Comando: dividir 10 0
# ❌ No se puede dividir por cero
#
# Comando: hola
# ❌ Comando no válido
#
# Comando: salir
# ¡Hasta pronto!
# ```

# TODO 1: Función que imprime las instrucciones del reto 1
def mostrar_instrucciones():
    print("\n--- Instrucciones de uso ---")
    print("Escribe uno de estos comandos para interactuar con el programa:")
    print("1. sumar x y --> Suma los valores x y")
    print("2. restar x y --> Resta los valores x y")
    print("3. multiplicar x y --> Multiplica los valores x y")
    print("4. dividir x y --> Divide los valores x y (cuidado con agregar '0' en y)")
    print("5. salir --> Salimos del programa")
    print("'x' es el primer número a introducir en el programa; 'y' es el segundo número a introducir")
    print("EJEMPLO: ")
    print("Comando: sumar 5 3")
    print("✅ 5 + 3 = 8")
    print("\nAhora bien, ¿empezamos?")

# TODO 2: Función de la lógica del programa reto1
def reto1():
    # Llamamos la función de las intrucciones
    mostrar_instrucciones()

    # Bucle principal while: ejecuta comandos hasta escribir la palabra 'salir'
    # El operador := (operador morsa) asigna valor a 'comando' y lo evalúa en la misma línea
    while (comando := input("\nComando: ").strip().lower()) != "salir":

        # Separar el comando en partes (en este caso 3)
        partes = comando.split()

        # Comprobar que 'partes' tenga dividida 3 partes (operador, x, y)
        if len(partes) != 3:
            print("❌ Comando no válido.")
            continue # Volver al inicio del bucle

        # Desempaquetamos las partes del comando
        operador, str_x, str_y = partes

        # Intentar que x y sean números flotantes
        try:
            x, y = float(str_x), float(str_y)
        except ValueError:
            print("❌ Números no válidos.")
            continue 

        # Ejecutar la operacion solicitada
        if operador == "sumar":
            print(f"✅ {x} + {y} = {x + y}")
            continue
        elif operador == "restar":
            print(f"✅ {x} + {y} = {x - y}")
            continue
        elif operador == "multiplicar":
            print(f"✅ {x} + {y} = {x * y}")
            continue
        elif operador == "dividir":
            if y != 0:
                print(f"✅ {x} + {y} = {x / y}")
                continue
            else:
                print("❌ No se puede dividir por 0.")
        else:
            print("❌ Comando no válido.")
    
    # Una vez introducido la palabra 'salir', finaliza el programa
    print("Hasta pronto 👋")

# TODO 3: Crear función principal
def main():
    # Imprimir título del reto 1
    print("--- 🛠️  Procesador interactivo de comandos 🛠️ ---")
    # Llamar función reto1
    reto1()

# TODO: Punto de entrada del programa
if __name__ == "__main__":
    main()