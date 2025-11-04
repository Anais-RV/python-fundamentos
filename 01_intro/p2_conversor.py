
numero=input("dame un numero: ");

try:
    numero=float(numero);
except ValueError:
    print("Error de conversor")


print (f"El valor es: {numero}")