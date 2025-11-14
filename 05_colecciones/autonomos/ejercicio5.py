# EJERCICIO AUTÓNOMO 5: Reporte de Gatos
# Enunciado: Imprime un reporte de gatos con `f-strings` a partir de un dict `{nombre: edad}`.

# TODO 1: Definir función que imprima un reporte de gatos
def reporte(dict):
    for i, gato in enumerate(dict, 1):
        print("----------------")
        print(f"{i}º Gato:")
        for clave, valor in gato.items():
            if clave == "nombre":
                print(f"Su {clave} es {valor}.")
        
            if clave == "edad":
                print(f"Tiene {valor} años.")
        

    print("----------------")

# TODO 2: Definir función principal
def main():
    print("--- Reporte de gatos ---\n")

    reporte_gatos = [
        {"nombre": "Michi", "edad": 24},
        {"nombre": "Leo", "edad": 3},
        {"nombre": "Nico", "edad": 8},
        {"nombre": "Chuchi", "edad": 3},
        {"nombre": "Chachito", "edad": 5},
    ]

    reporte(reporte_gatos)


# TODO 3: Punto de entrada del programa
if __name__ == "__main__":
    main()

# RESULTADO:
# --- Reporte de gatos ---
#
# ----------------
# 1º Gato:
# Su nombre es Michi.
# Tiene 24 años.
# ----------------
# 2º Gato:
# Su nombre es Leo.
# Tiene 3 años.
# ----------------
# 3º Gato:
# Su nombre es Nico.
# Tiene 8 años.
# ----------------
# 4º Gato:
# Su nombre es Chuchi.
# Tiene 3 años.
# ----------------
# 5º Gato:
# Su nombre es Chachito.
# Tiene 5 años.
# ----------------
# Éxito ✅