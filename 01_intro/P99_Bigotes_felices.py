nombre=input("Como se llama: ")

edad=input("Edad que tiene: ")

try:
    edad=float(edad)
except ValueError:
    print ("--Edad inválida--")
    edad="edad desconocida";

print(f"Se llama {nombre} y tiene {edad}.")