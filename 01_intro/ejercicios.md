# Ejercicios 01_intro

Tiempo estimado: 2–3h

---

## 🎯 Ejercicio guiado: La Calculadora que Crece (v1)

Ejercicio progresivo que evoluciona en cada módulo. En esta versión: calculadora básica con suma.

👉 **[Ver guía completa: ejercicio_guiado/GUIA.md](./ejercicio_guiado/GUIA.md)**

---

## Guiado 1: Tu primer script
Objetivo: imprimir un saludo y una variable.

Paso 1: Crea un archivo `primer_script.py`.
Paso 2: Declara una variable `nombre = "Ana"`.
Paso 3: Imprime `Hola, Python` y luego `Hola, {nombre}` usando f-strings.
Paso 4: Ejecuta el script y valida la salida.

Errores comunes: olvidar `f` en f-strings, usar comillas inconsistentes.

## Guiado 2: Input del usuario
Objetivo: leer un nombre y saludarlo.

Paso 1: Crea `saludo_input.py`.
Paso 2: Usa `input("¿Cómo te llamas? ")` para leer.
Paso 3: Imprime `Hola, <nombre>` con f-string.
Paso 4: Valida entradas vacías: si el usuario no escribe nada, imprime `Nombre no válido`.

Errores comunes: no convertir tipos, no validar entrada vacía.

## Autónomos
1. Crea `variables_basicas.py` que combine nombre y ciudad en un string: `"Ana vive en Lima"`.
2. Crea `conversor.py` que pida un número y lo convierta a float, manejando ValueError con un mensaje amable.
3. Crea `tres_prints.py` que imprima tres líneas con información personal.
4. Crea `eco.py` que repita lo que el usuario escribe (usa input y print).

## Desafío: Bigotes Felices (refugio)
En el refugio Bigotes Felices quieren un script que pida el nombre del gato y su edad, y muestre: `Gato: <nombre> (edad: <edad>)`. Si la edad no es un número, muestra `Edad inválida`.

Errores comunes: no validar entrada, no manejar excepciones.

Tiempo estimado: 2–3h
