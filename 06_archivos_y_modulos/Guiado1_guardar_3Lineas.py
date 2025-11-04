

gatos = "gato 1","gato 2","gato 3"

ruta="./escribir.txt"


#guardar
with open(ruta,"w",encoding="UTF-8") as f:
    for g in gatos:
        f.write(f"{g}\n")
    f.close()




        