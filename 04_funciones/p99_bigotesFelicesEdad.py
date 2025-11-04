
gatos=[{"nombre":"Garfield","edad":5},
       {"nombre":"Neko","edad":2},
       {"nombre":"Saturno","edad":7},
       {"nombre":"sardina","edad":1},
       {"nombre":"Brujo","edad":19},
       ]

edad=5;
print (f"\nGatos con mas de {edad} años \n");

for cat in gatos:
    if (cat["edad"]>edad):
        print(cat["nombre"],cat["edad"], " años")
    