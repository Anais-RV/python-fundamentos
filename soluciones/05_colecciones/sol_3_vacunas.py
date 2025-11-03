# En Python, un set es una colección sin elementos duplicados y sin orden específico.
vacunas = {"Pfizer", "Moderna", "AstraZeneca", "Sputnik", "Sinovac"}

print("Vacunas disponibles:", vacunas)

nombre = input("Escribe el nombre de una vacuna: ")

if nombre in vacunas:
    print(f"✅ La vacuna '{nombre}' está en la lista.")
else:
    print(f"❌ La vacuna '{nombre}' no está registrada.")