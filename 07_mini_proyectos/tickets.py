## 2) Mini sistema de tickets
#- Usa listas y diccionarios para manejar tickets (id, título, estado).
#- Operaciones: crear, listar, cerrar.
#- Persistencia opcional en archivo.
id=9;

tickets=[
    {1,"Vampiros","en Curso"},
    {2,"pinguinos","en Curso"},
    {3,"bella","en Curso"},
    {4,"Pinocho","Caducado"},
    {5,"Gnomos","en Curso"},
    {6,"Ogros III","en Curso"},
    {7,"robot la venganza","Caducado"},
    {9,"robot II, la continuacion de la venganza","en Curso"},
    ]

def menu():

    while(True):
        print("1: Anadir Pelicula:  ")
        print("2: Listar Peliculas: ")
        print("3: Cambiar estado:   ")
        opcion = input("¿Que opcion quieres?: ")
        
        pelicula=input("Dame el nombre de la pelicula?")
        pelicula=input("Dame el nombre de la pelicula?")
