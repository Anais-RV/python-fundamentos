import json

gatos=[{"nombre":"Garfield","edad":5},
       {"nombre":"Neko","edad":2},
       {"nombre":"Saturno","edad":7},
       {"nombre":"sardina","edad":1},
       {"nombre":"Gato de brujo","edad":19},
       ]


#guardar diccionario

ruta = "P1_gatos.csv"
with open(ruta, "w", encoding="utf-8") as f:
    for g in gatos:
        f.write(f"{g}")

    f.close()




#Mostrar
with open(ruta, "r", encoding="utf-8") as x:
    for i, linea in enumerate(x, start=1):
        print(f"{i}: {linea.strip()}")

