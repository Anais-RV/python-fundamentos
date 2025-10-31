"""
Calculadora v1 - Suma básica
=============================

En esta primera versión crearás una calculadora simple que solo suma dos números.

Conceptos aplicados:
- Variables
- input() para leer datos del usuario
- print() para mostrar resultados
- Conversión de tipos (float())

Instrucciones:
1. Pide al usuario el primer número
2. Pide al usuario el segundo número
3. Convierte ambos a números decimales (float)
4. Suma los dos números
5. Muestra el resultado
"""

# TODO 1: Pide el primer número al usuario
# Pista: usa input() y guarda el valor en una variable
# primer_numero = ...
primer_numero = input("Ingrese un número: ")

# TODO 2: Pide el segundo número al usuario
# segundo_numero = ...
segundo_numero = input("Ingrese otro número: ")

# TODO 3: Convierte los strings a números decimales
# Pista: usa float() para permitir decimales (ej: 3.5)
# num1 = float(primer_numero)
# num2 = ...
num_float1 = float(primer_numero)
num_float2 = float(segundo_numero)

# TODO 4: Realiza la suma
# resultado = ...
resultado = num_float1 + num_float2

# TODO 5: Muestra el resultado
# Pista: print("El resultado es:", resultado)
print(f"{num_float1} + {num_float2} = {resultado}")

# ¡Ya está! Ejecuta el programa y prueba con diferentes números
# Ejemplos para probar:
# - 5 y 3 → debe dar 8
# - -2 y 7 → debe dar 5
# - 3.5 y 2.5 → debe dar 6.0
#
# Prueba:
# Comando a ejecutar: 'python calculadora_v1.py'
# Resultado:
# Ingrese un número: 4
# Ingrese otro número: 9
# 4.0 + 9.0 = 13.0
# Éxito ✅ 