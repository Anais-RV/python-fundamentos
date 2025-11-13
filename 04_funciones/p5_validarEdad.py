
edad=input("Dame una edad: ");

try:
    edad=int(edad);
    if (edad>=0):
        print (f"la edad es: {edad}")
    else:
        print ("no puede ser negativa la edad")

except ValueError:
    print(f"-- ERROR, '{edad}'. No es un valor valido --")

