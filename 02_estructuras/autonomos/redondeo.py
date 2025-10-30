# EJERCICIO AUTÓNOMO 3: REDONDEO
# Enunciado: redondea 3.14159 a 3 decimales.

# Variable num con el número específico a redondear
num = 3.14159

# Variable num_redondo que redondea variable num a 3 decimales
# round(): devuelve un número con decimales que es una versión redondeada del
#          mismo, con el número especificado de decimales.
# Sintaxis: round(number, digits)
# number --> Obligatorio. El número a ser redondeado
# digits --> Opcional. El número específico a usar para redondear 
#            number. Por defecto es 0.
num_redondo = round(num, 3)

# Imprimir resultado del ejercicio
print(f"Número: {num}")
print(f"Número redondeado a 3 decimales: {num_redondo}")

# Test: ejecutar 'python redondeo.py
# Resultado esperado:
# Número: 3.14159
# Número redondeado a 3 decimales: 3.142
# Éxito ✅ 