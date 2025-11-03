texto = "banana"
conteo = {}

for letra in texto:
    conteo[letra] = conteo.get(letra, 0) + 1

print(conteo)