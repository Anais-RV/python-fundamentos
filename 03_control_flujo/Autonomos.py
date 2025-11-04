



## Autónomos

#1. Recorre una lista de gatos y imprime sus nombres.

listagatos={"Isidoro","neko", "salchipapa","Garfield","Meow"}

for nombre  in listagatos:
    print(nombre)
#2. Cuenta letras en un string usando un bucle.

contaLetras="buho"

i=0
while(i<len(contaLetras)):
    print(contaLetras[i]);
    i+=1;

print (f"contiene {i} letras en total" )


#3. Genera una tabla de multiplicar del 1 al 5 usando `for` anidados.

for  i in range (6):
    print("")
    for  e in range (11):
        print(f"{i} x {e} = {i*e} ")
        

#4. Pide contraseñas hasta que sea `gato123`.

contrasena="gato123";
password=" ";

while(password !=contrasena):
    password=input("escrible la contraseña: ");
    
    if(password !=contrasena):
        print("errona, escribe otra")

password=input("Pass Aceptada");


## Desafío: Bigotes Felices (turnos)
#Dado un número de gatos y dos cuidadores, asigna alternadamente gatos a Turno A y B.

#Tiempo estimado: 3–4h
#Errores comunes: condiciones mal anidadas, bucles infinitos, no validar entradas.

#Errores comunes: condiciones mal anidadas, bucles infinitos.
