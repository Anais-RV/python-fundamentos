gatos="Azulina","Bako","Amantina","Benko","Alisa","Brisa","Aquamarina","Bola de nieve II","Aguarras",

cuidadorA=[]
cuidadorB=[]

posicion=0;
for i in gatos:
 
    if(posicion%2==0):
        cuidadorA.append(i)
    else: 
        cuidadorB.append(i)

    posicion+=1

print("\nCuidador A: ")
for A in cuidadorA:
    print("\t"+A)

print("\nCuidador B: ")
for B in cuidadorB:
    print("\t"+B)