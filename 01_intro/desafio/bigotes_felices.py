# Desafio: Bigotes Felices
# En el refugio Bigotes Felices quieren un script que pida el nombre del gato y su edad, 
# y muestre: `Gato: <nombre> (edad: <edad>)`. 
# Si la edad no es un número, muestra `Edad inválida`. 

nombre_gato = input("Nombre del gato --> ")

edad_gato = input("Edad del gato --> ")

try: 
    edad_gato = int(edad_gato)

    datos = f"Gato: {nombre_gato} (edad: {edad_gato})"

    print(datos)

except ValueError:
    print("Edad inválida")

# Primer test: imprimir datos introducidos de tipo string. Completado ✅
# Segundo test: imprimir datos de nombre_gato (string: cadena de texto) y de edad_gato (int: numero entero)
# Prueba: 
# Nombre del gato --> pepe
# Edad del gato --> julio
# Error ❌
# Mensaje enviado: Edad inválida