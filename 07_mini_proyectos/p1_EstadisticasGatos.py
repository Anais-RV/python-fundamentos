## 1) Estadísticas del refugio de gatos
#- Entrada: archivo o lista de pesos y edades.
#- Tareas: conteo, media, mediana simple, top-k más pesados.
#- Salida: resumen por pantalla y guardado opcional a archivo.
import p1_funciones 

#variables
gatos=[
       {"nombre":"Luna",            "kg":5,     "edad":3},
       {"nombre":"Michi",           "kg":10,    "edad":9},
       {"nombre":"Bola de nieve II","kg":15,    "edad":6},
       ]

ruta="gatos.txt"

informacion=[]
#main
informacion.append( f"Conteos de gatos:          {p1_funciones.contador(gatos)}\n" )
informacion.append("Peso medio de los gatos:   {p1_funciones.media(gatos)}\n")
informacion.append(f"Peso mediana de los gatos: {p1_funciones.mediana(gatos)}\n")
informacion.append(p1_funciones.GatoMasPesado(gatos))
p1_funciones.guardarGatos(ruta,informacion)
p1_funciones.leerGatos(ruta)








