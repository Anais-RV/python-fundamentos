# EJERCICIO AUTÓNOMO 1: Vacunas
# Enunciado: Conjunto de vacunas (set) y prueba de pertenencia.

# TODO 1: Crear conjunto de vacunas (set)
vacunas = {"rabia", "gripe", "hepatitis B", "tuberculosis"}

# TODO 2: Crear función principal
def main():
    # TODO 2.1: Imprimir título del ejercicio
    print("\n--- Lista de Vacunas ---")
    # TODO 2.2: Hacer prueba booleana usando 'in'
    print(f"1. Vacuna contra la rabia: {'rabia' in vacunas}")
    print(f"2. Vacuna contra la gastroenteritis: {'gastroenteritis' in vacunas}")
    print(f"3. Vacuna contra la gripe: {'gripe' in vacunas}")
    print(f"4. Vacuna contra la hepatitis B: {'hepatitis b' in vacunas}")
    print(f"5. Vacuna contra la tuberculosis: {'tuberculosis' in vacunas}")
    print(f"6. Vacuna contra la varicela: {'varicela' in vacunas}")
    print(f"7. Vacuna contra el tétanos: {'tetanos' in vacunas}")

# TODO 3: Punto de entrada del programa
if __name__ == "__main__":
    main()

# RESULTADO:
# --- Lista de Vacunas ---
# 1. Vacuna contra la rabia: True
# 2. Vacuna contra la gastroenteritis: False
# 3. Vacuna contra la gripe: True
# 4. Vacuna contra la hepatitis B: False
# 5. Vacuna contra la tuberculosis: True
# 6. Vacuna contra la varicela: False
# 7. Vacuna contra el tétanos: False
# -------------------------------------------
# Éxito ✅