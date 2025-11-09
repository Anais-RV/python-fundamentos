# EJERCICIO AUTÓNOMO 3: Ocurrencias de letras
# Enunciado: Cuenta ocurrencias de letras en un string con un dict.

# TODO 1: Crear función que devuelva un diccionario de caractéres de un texto específico
def contar_letras(texto):

    # TODO 1.2: Comprobar si el texto está vacío o no
    if not texto:
        print("El texto está vacío.")
        return
    
    # TODO 1.3: Comprobar si el texto tiene sólo espacios en blanco usando isspace()
    if texto.isspace():
        print("El texto recibido sólo tiene espacios en blanco.")
        return

    # TODO 1.4: 
    # Una vez pasadas las 2 comprobaciones, declarar dict vacío 
    # para después enumerar cuántas letras hay en el texto
    contador = {}
    # TODO 1.5: Imprimir texto solicitado
    print(f"\nTexto recibido: {texto}\n")

    # TODO 1.6: Imprimir título de recorrido de letras antes del bucle
    print(f"--- Recorriendo texto sin contar espacios... ---")
    # TODO 1.7: Empezar bucle for que enumera las letras del texto
    for i, letra in enumerate(texto, 1):
        # TODO 1.7.1: Convertir las letras en minúsculas usando lower()
        letra_min = letra.lower()
        # TODO 1.7.2: Contar letras (ignoramos espacios y otros caracteres usando isalpha())
        if letra_min.isalpha():
            # TODO 1.7.3: Imprimir recorrido de la lista sin contar espacios ni otros caracteres
            print(f"{i}: {letra}")

            # TODO 1.7.4: Verificar si la letra ya existe en el diccionario
            if letra_min in contador:
                # TODO 1.7.5: Aumentar su contador si la letra ya existe
                contador[letra_min] += 1
            else:
                # TODO 1.7.6: Crear con valor 1 si la letra NO existe todavía
                contador[letra_min] = 1
    
    # TODO 1.8: Retornar el diccionario con las letras recorridas
    return contador

# TODO 2: Crear funcion que muestre los resultados del contador
def mostrar_ocurrencias(contador):

    # TODO 2.1: Comprobar si hay contenido en el contador o no
    if not contador:
        print("No hay letras de texto para contar.")
        return
    # TODO 2.2: Seguir adelante si hay contenido
    else:
        # TODO 2.3: Imprimir contador 
        print(f"\nDiccionario con ocurrecias de letras: {contador}")
        # TODO 2.4: Imprimir título del recorrido del diccionario del contador
        print("\n--- Recorriendo diccionario... ---")

        # TODO 2.5: Empezar bucle for que recorre el contador de letras
        for i, letra in enumerate(contador, 1):
            # TODO 2.5.1: Comprobar si el número de veces que ha contado en cada carácter es 1 o más
            if contador[letra] == 1:
                # TODO 2.5.2: Imprimir que se ha contado una vez si el número de veces es 1.
                print(f"Letra nº{i}: {letra} | Se ha contado {contador[letra]} vez.")
            else:
                # TODO 2.5.3: Imprimir que se contó muchas veces si el número es superior a 1. 
                print(f"Letra nº{i}: {letra} | Se han contado {contador[letra]} veces.")
        
        # TODO 2.6: Imprimir final del recorrido
        print("\nFinal del recorrido!!")

# TODO 3: Crear función principal
def main():
    # TODO 3.1: Imprimir título del ejercicio
    print("--- Contador de letras ---")
    # TODO 3.2: Pedir al usuario una frase
    texto = input("\nIntroduce una frase --> ")
    # TODO 3.3: Declarar variable para retornar un diccionario del texto pedido
    contador = contar_letras(texto)
    # Todo 3.4: Función para mostrar recorrido de las letras del texto
    mostrar_ocurrencias(contador)


# TODO 4: Punto de entrada del programa
if __name__ == "__main__":
    main()