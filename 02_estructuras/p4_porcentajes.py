print ("Dame un numero");
try:
    numero=float(input())
finally:
    print ("conversion fallida");

print(f"El 15%  de {numero} es {round(numero*1.15,2)}")