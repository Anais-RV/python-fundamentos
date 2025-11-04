# DESAFIO: Bigotes Felices (turnos)
# Enunciado: Dado un número de gatos y dos cuidadores, asigna alternadamente gatos a Turno A y B.

# TODO 0: Imprimir título y descripción del ejercicio
print("---- BIGOTES FELICES ----")
print("-- Asignación de gatos por turnos --")

# TODO 1: Bucle while que se repite hasta insertar un número de gatos que sea mayor que 0
while True:
    # TODO 2: Intentar convertir 'gatos' a int a la hora que pida el programa al usuario
    try: 
        # TODO 3: Pedir un número de gatos al usuario
        gatos = int(input("\nIntroduce un número de gatos --> "))

        # TODO 4: Condicional si el numero introducido es 0 o menor y se repetiría el bucle while
        if gatos <= 0:
            print("Debe ingresar al menos 1 gato para la lista de asignacion.")
            continue
        # TODO 5: Condicional si se asigna un numero específico de gatos se mostraría una lista de turnos
        else:
            # TODO 6: Imprimir lista
            print(f"\nLista de asignación para {gatos} gatos")
            print("---------------------")
            # TODO 7: Agregar contadores para el número de turnos que tiene cada cuidador
            cuidador_a = 0
            cuidador_b = 0

            # TODO 8: Añadir bucle for para recorrer el numero de gatos introducido
            for i in range(1, gatos + 1):
                # TODO 9: Condicional si el numero recorrido es par se le asignará al cuidador A
                if i % 2 == 0:
                    print(f"{i}º gato | Cuidador A")
                    cuidador_a += 1
                # TODO 10: Condicional si el numero recorrido es impar se le asignará al cuidador B
                else:
                    print(f"{i}º gato | Cuidador B")
                    cuidador_b += 1
            # TODO 11: Una vez recorrido la lista, salir del bucle while        
            break
            
    # TODO 12: Mostrar mensaje de error si el valor introducido por el programa no es un número
    except ValueError:
        print("ERROR ❌. No ha insertado un número de gatos.")
        continue

# TODO 13: Imprimir cantidad de gatos y el número de turnos de cada cuidador
print(f"\nNúmero de gatos: {gatos}")
print(f"Número de gatos para la cuidadora A: {cuidador_a}")
print(f"Número de gatos para la cuidadora B: {cuidador_b}")

# RESULTADO:
# ---- BIGOTES FELICES ----
# -- Asignación de gatos por turnos --
#
#Introduce un número de gatos --> 6
# 
# Lista de asignación para 6 gatos
# ---------------------
# 1º gato | Cuidador B
# 2º gato | Cuidador A
# 3º gato | Cuidador B
# 4º gato | Cuidador A
# 5º gato | Cuidador B
# 6º gato | Cuidador A
# 
# Número de gatos: 6
# Número de gatos para la cuidadora A: 3
# Número de gatos para la cuidadora B: 3