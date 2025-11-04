
def contador(g):
    contador=0;
    for i in g:
        contador+=1;
    return(contador);

    
def media(g):
    total = sum(gato["kg"] for gato in g)
    if(total==0):
        return 0;
    return(total/len(g));

def mediana(g):
    pesos = sorted(gato["kg"] for gato in g)
    n = len(pesos)
    if n % 2 == 1:
        return pesos[n // 2]
    else:
        return (pesos[n // 2 - 1] + pesos[n // 2]) / 2
    
def GatoMasPesado(g):
    pesoMax=0;
    GatoMasPesado="";
    for i in g:
        if i["kg"]>pesoMax:
            pesoMax=float(i["kg"])
            GatoMasPesado=i["nombre"];

    return (f"--{GatoMasPesado} es el felino con mas peso es con {pesoMax} Kg." )


def guardarGatos(ruta,info):
    with open(ruta, 'w', encoding='utf-8') as archivo:
        archivo.write(f"{info}")

def leerGatos(ruta):
    print("\tleyendo Gatos: ")
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                print ( f"{linea} \n" );
    except FileNotFoundError:
            print(f"El archivo '{ruta}' no existe.")