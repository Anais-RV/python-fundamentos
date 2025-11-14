def es_par(n):
    if not isinstance(n, int):
        raise TypeError("n debe ser un número entero")
    return n % 2 == 0

def es_par_ans(ans):
    if ans == True:
        print("Tu número es PAR")
    elif ans != True:
        print("Tu número es IMPAR")
    else:
        print("¡Ha habido un error!")

print("Dame un número (int):")
user_n_input = input()
user_n = int(user_n_input)
answer = es_par(user_n)
es_par_ans(answer)