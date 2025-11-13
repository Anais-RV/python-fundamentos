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
print("Dame el primer valor: ")
valor1=input()

# TODO 2: Pide el segundo número al usuario
# segundo_numero = ...
print("Dame el segundo valor: ")
valor2=input()

# TODO 3: Convierte los strings a números decimales
# Pista: usa float() para permitir decimales (ej: 3.5)
# num1 = float(primer_numero)
# num2 = ...

valor1=float(valor1);
valor2=float(valor2);

# TODO 4: Realiza la suma
# resultado = ...

suma= valor1+valor2;

# TODO 5: Muestra el resultado
# Pista: print("El resultado es:", resultado)

print (suma);
# ¡Ya está! Ejecuta el programa y prueba con diferentes números
# Ejemplos para probar:
# - 5 y 3 → debe dar 8
# - -2 y 7 → debe dar 5
# - 3.5 y 2.5 → debe dar 6.0
