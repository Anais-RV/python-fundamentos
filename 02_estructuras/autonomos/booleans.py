# EJERCICIO AUTÓNOMO 1: BOOLEANS
# Enunciado: evalúa condiciones simples (>=, ==) y muestra True/False.

num1 = 4
num2 = 6

mayorigualque = num1 >= num2
menorigualque = num1 <= num2
igualque = num1 == num2
distintoque = num1 != num2
mayorque = num1 > num2
menorque = num1 < num2

print(f"CONDICIONES SIMPLES:")
print(f"{num1} >= {num2} : {mayorigualque}")
print(f"{num1} <= {num2} : {menorigualque}")
print(f"{num1} == {num2} : {igualque}")
print(f"{num1} != {num2} : {distintoque}")
print(f"{num1} > {num2} : {mayorque}")
print(f"{num1} < {num2} : {menorque}")