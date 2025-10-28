numero_conv = input("Introduce un número a convertirlo en float")

print(f"Número introducido: {numero_conv}")
print(f"Tipo de dato: {type(numero_conv)}")

try:
    numero_conv = float(numero_conv)
    print(f"Perfecto! Se ha convertido {numero_conv} en un valor float: {type(numero_conv)}")
except ValueError:
    print(f"Lo siento! '{numero_conv}' no es un número válido. Por favor, vuelva a ejecutar de nuevo el archivo")

# Conversion valor 45 convertido a float con éxito ✅

# Conversion valor 'pepe' convertido a float fallo ❌
# Razón: ValueError: could not convert string to float: 'pepe'