# EJERCICIO GUIADO 1: Diccionario simple
# ENUNCIADO: Crea un dict con `{"nombre": "Mishi", "edad": 3}` 
#            y accede a sus claves de forma segura con `get`.

# TODO 1: Crear diccionario con los datos concretos
dict_gato = {"nombre": "Mishi", "edad": 3}

# TODO 2: Crear función principal
def main():
    # TODO 2.1: Imprimir título del ejercicio y línea divisoria del principio
    print("--- Diccionario del gato ---")
    print("----------------------------")
    # TODO 2.2: Acceder a la clave 'nombre' del diccionario e imprimir
    # get() devuelve el valor de una clave específica
    # nombre devuelve el valor de la clave 'nombre'
    nombre = dict_gato.get('nombre')
    print(f"1. Nombre | {nombre}")

    # TODO 2.3: Acceder a la clave 'edad' del diccionario e imprimir
    # edad devuelve el valor de la clave 'edad'
    edad = dict_gato.get('edad')
    print(f"2. Edad | {edad} años")

    # TODO 2.4: Acceder a la clave 'peso' del diccionario e imprimir
    # peso devuelve el valor de la clave 'peso'
    # si no existe, devuelve el valor predeterminado 'None'
    peso = dict_gato.get('peso')
    print(f"3. Peso | {peso} Kg")

    # TODO 2.5: Acceder a la clave 'color' del diccionario e imprimir
    # color devuelve el valor de la clave 'color'
    # si no existe, devuelve el valor predeterminado 'No registrado'
    color =  dict_gato.get('color', "No registrado")
    print(f"4. Color | {color}")
    # TODO 2.6: Imprimir línea divisoria del final
    print("----------------------------")

# TODO 3: Punto de entrada del programa
if __name__ == "__main__":
    main()

# RESULTADO:
# --- Diccionario del gato ---
# ----------------------------
# 1. Nombre | Mishi
# 2. Edad | 3 años
# 3. Peso | None Kg
# 4. Color | No registrado
# ---------------------------- 
# Éxito ✅