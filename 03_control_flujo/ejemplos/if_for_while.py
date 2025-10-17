"""Condicionales y bucles básicos sin magia."""

x = 3
if x > 0:
    print("positivo")
elif x == 0:
    print("cero")
else:
    print("negativo")

for i in range(3):
    print(f"i={i}")

n = 3
while n > 0:
    print(n)
    n -= 1
