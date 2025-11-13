def esPar(a):

    valor=int(a)

    if (valor%2)==0:
        print("Es par")
    else:
        print("Es IMPAR")



numero=input("Dame un numeor para comprobar si es par o no: ");

try:
    esPar(int(numero))
except ValueError:
    print("No es un numero valido")


