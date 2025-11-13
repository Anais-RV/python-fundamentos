numero = 0;
suma = 0;
contador = 0;

while True:
    print("Dame un numero \n  -1 para salir:");
    numero = float(input());
    
    if numero == -1:
        break ;
    
    suma += numero;
    contador += 1;

if contador > 0:
    print("El promedio es:", suma / contador);
else:
    print("No ingresaste ningun numero valido.");
