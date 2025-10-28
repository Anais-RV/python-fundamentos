# 1
vacunas = {"rabia", "leucemia", "panleucopenia"}
print("rabia" in vacunas) #sería verdadero: True.
print("parvovirus" in vacunas) #sería falso: False.

# 2
nombres = ["Michifuchi", "Peludo", "Catanga", "Furro"]
edades = [3, 7, 1, 18]
michis = dict(zip(nombres, edades))
print(michis)

# 3
texto = "Soy un michi feliz"
contador = {}
for letra in texto:
    if letra != " ":
        contador[letra] = contador.get(letra, 0) + 1
print(contador)

# 4
michis = ["Michifuchi", "Fuchimichi", "Pelúo", "Garra mortal"]
ultimos = michis[-3]
print(ultimos)

michi_Mayus = [nombre.upper() for nombre in michis]
print(michi_Mayus)

# 5
michis = {"Michifurri": 14, "Pelúo": 32, "Garra mortal": 2}
for nombre, edad in michis.items():
    print(f"{nombre} tiene {edad} años.")