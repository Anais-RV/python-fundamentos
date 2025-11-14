# EJERCICIO AUTÓNOMO 2: Contar letras
# Enunciado: Cuenta letras en un string usando un bucle.

# TODO 0: Imprimir título del programa
print("---- Cuenta Letras ---- \n")

# TODO 1: Pedir al usuario unas palabras
string = input("Escribe unas palabras --> ")

# TODO 2: Iniciar un contador para las letras
count = 0

# TODO 3: Iniciar bucle for para recorrer cada caracter del string
print("Caracter --> Número")
for i in string:
    # TODO 4: Incrementar el contador en 1 cada caracter que recorre 
    count += 1
    # TODO 5: Imprimir indice y letra del string recorrido
    print(f"{i} --> {count}")
    

# TODO 6: Imprimir total del contador
print(f"Letras contadas: {count}")