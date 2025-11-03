nombres = ["Ana", "Luis", "María", "Carlos", "Elena"]

print(f"Del índice 1 al 3: {nombres[1:4]}")
print(f"Desde el inicio hasta el 3 (sin incluirlo): {nombres[:3]}")
print(f"Desde el 2 hasta el final: {nombres[2:]}")
print(f"Últimos 2 elementos: {nombres[-2:]}")
print(f"Cada 2 elementos: {nombres[::2]}")
print(f"Lista invertida: {nombres[::-1]}")


#Crear una lista de cuadrados:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cuadrados = [n ** 2 for n in numeros]
print(cuadrados)


#Filtrar solo los números pares:
pares = [n for n in numeros if n % 2 == 0]
print(pares)


#Convertir una lista de nombres a mayúsculas:
mayus = [nombre.upper() for nombre in nombres]
print(mayus)


#Extraer vocales de una cadena:
texto = "python"
vocales = [letra for letra in texto if letra in "aeiou"]
print(vocales)


pares_invertidos = [n for n in numeros[::-1] if n % 2 == 0]
print(pares_invertidos)