# Desafio: Bigotes Felices
# En el refugio Bigotes Felices quieren un script que pida el nombre del gato y su edad, 
# y muestre: `Gato: <nombre> (edad: <edad>)`. 
# Si la edad no es un número, muestra `Edad inválida`. 

# Variable nombre_gato a introducir dato string
nombre_gato = input("Nombre del gato --> ")

# Variable edad_gato a introducir dato int
edad_gato = input("Edad del gato --> ")

try: 
    # Intentamos convertir valor str a int
    edad_gato = int(edad_gato)

    # Variable datos a mostrar mensaje de los datos introducidos por el usuario
    datos = f"Gato: {nombre_gato} (edad: {edad_gato})"

    # Imprimir mensaje de salida
    print(datos)

except ValueError:
    print("Edad inválida")

# Primer test: imprimir datos introducidos de tipo string.
# Prueba: 
# Nombre del gato --> pepe
# Edad del gato --> viyuela
# Mensaje de salida: Gato: pepe (edad: viyuela) ✅

# Segundo test: imprimir datos de nombre_gato (string: cadena de texto) y de edad_gato (int: numero entero)
# Prueba: 
# Nombre del gato --> pepe
# Edad del gato --> julio
# Mensaje de salida: Edad inválida ❌

# Tercer test: imprimir los datos validando try/except
# Prueba: 
# Nombre del gato --> pepe
# Edad del gato --> 10
# Mensaje de salida: Gato: pepe (edad: 10) ✅