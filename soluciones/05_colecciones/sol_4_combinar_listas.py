nombres = ["Ana", "Luis", "María", "Carlos"]
edades = [25, 30, 22, 28]

personas = dict(zip(nombres, edades))

if len(nombres) != len(edades):
    print("⚠️ Las listas no tienen la misma cantidad de elementos")

print("Diccionario combinado:")
for nombre, edad in personas.items():
    print(f"{nombre} tiene {edad} años.")