nombre = [
    {"nombre": "Garfield"},
    {"nombre": "Neko"},
    {"nombre": "Saturno"},
    {"nombre": "Sardina"},
    {"nombre": "Brujo"},
]

edades = [
    {"edad": 7},
    {"edad": 4},
    {"edad": 8},
    {"edad": 9},
    {"edad": 3},
]

ficha = []


for n, e in zip(nombre, edades):
    ficha.append(f"{n['nombre']}, {e['edad']} años")

for f in ficha:
    print(f)
