# 🦭 Calculadora v7 - Refactorización con Operador Morsa

## 🎯 Objetivo

Aprenderás a **refactorizar código existente** aplicando el operador morsa (`:=`) para:
- ✅ Reducir código repetitivo
- ✅ Mejorar la legibilidad
- ✅ Aplicar features modernos de Python 3.8+

**Tiempo estimado**: 60-90 minutos

---

## 📋 Requisitos previos

Antes de empezar, asegúrate de:
- ✅ Haber completado la calculadora v6 (persistencia JSON)
- ✅ Haber leído [`cheatsheets/07_operador_morsa.md`](../../cheatsheets/07_operador_morsa.md)
- ✅ Tener Python 3.8 o superior

---

## 🔍 ¿Qué vamos a refactorizar?

En la calculadora v6 hay **varios lugares** donde repetimos código o hacemos cálculos innecesarios. El operador morsa nos ayudará a simplificar:

### 1️⃣ Bucle principal con input
**Antes (v6):**
```python
mostrar_menu()
opcion = input("\nElige una opción: ")

if opcion == "7":
    # ...
```

**Después (v7):**
```python
while (opcion := input("\n=== CALCULADORA ===\n1. Sumar\n2. Restar\n...\n7. Salir\n\nElige una opción: ")) != "7":
    # El bucle continúa hasta que el usuario elija salir
```

### 2️⃣ Validación de opción
**Antes (v6):**
```python
opcion = input("\nElige una opción: ")
if opcion not in ["1", "2", "3", "4", "5", "6"]:
    print("❌ Opción no válida")
    continue
```

**Después (v7):**
```python
if not (opcion.isdigit() and 1 <= (opcion_num := int(opcion)) <= 6):
    print("❌ Opción no válida")
    continue
```

### 3️⃣ Confirmación con input
**Antes (v6):**
```python
confirmacion = input("⚠️  ¿Estás seguro? (s/n): ")
if confirmacion.lower() != "s":
    print("❌ Operación cancelada")
    return
```

**Después (v7):**
```python
if (confirmacion := input("⚠️  ¿Estás seguro? (s/n): ").lower()) != "s":
    print("❌ Operación cancelada")
    return
```

### 4️⃣ Obtener números con validación
**Antes (v6):**
```python
def obtener_numeros():
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))
    return num1, num2
```

**Después (v7):**
```python
def obtener_numeros():
    """Pide dos números validados al usuario."""
    while not (entrada1 := input("Primer número: ")).replace(".", "", 1).replace("-", "", 1).isdigit():
        print("❌ Ingresa un número válido")
    
    while not (entrada2 := input("Segundo número: ")).replace(".", "", 1).replace("-", "", 1).isdigit():
        print("❌ Ingresa un número válido")
    
    return float(entrada1), float(entrada2)
```

---

## 📝 Instrucciones paso a paso

### Paso 1: Copia la calculadora v6
```bash
# Copia tu calculadora v6 completada
cp 06_archivos_y_modulos/ejercicio_guiado/calculadora_v6.py 07_mini_proyectos/ejercicio_guiado/calculadora_v7.py
```

O crea el archivo `calculadora_v7.py` con el código base que te proporcionamos.

### Paso 2: Actualiza el docstring
Cambia la primera línea del docstring:
```python
"""
Calculadora v7 - Refactorización con Operador Morsa
====================================================

Esta versión refactoriza la v6 aplicando el operador morsa (:=) para:
- Reducir código repetitivo
- Mejorar la legibilidad en validaciones
- Aplicar sintaxis moderna de Python 3.8+

Conceptos aplicados:
- Operador morsa (:=) en bucles while
- Operador morsa en condicionales
- Operador morsa en validaciones
- Refactorización de código existente
"""
```

### Paso 3: Refactoriza `obtener_numeros()`
Mejora la validación usando el operador morsa:

```python
def obtener_numeros():
    """Pide dos números al usuario con validación mejorada."""
    
    # TODO 1: Usa operador morsa para validar y asignar en una línea
    while True:
        entrada1 = input("Primer número: ")
        try:
            num1 = float(entrada1)
            break
        except ValueError:
            print("❌ Ingresa un número válido")
    
    while True:
        entrada2 = input("Segundo número: ")
        try:
            num2 = float(entrada2)
            break
        except ValueError:
            print("❌ Ingresa un número válido")
    
    return num1, num2
```

**Pista**: Puedes usar `try-except` dentro de una condición con el operador morsa.

### Paso 4: Refactoriza `limpiar_historial()`
Simplifica la confirmación:

```python
def limpiar_historial():
    """Limpia el historial en memoria y elimina el archivo."""
    global historial
    
    # TODO 2: Refactoriza la confirmación con operador morsa
    confirmacion = input("⚠️  ¿Estás seguro de que quieres limpiar el historial? (s/n): ")
    if confirmacion.lower() != "s":
        print("❌ Operación cancelada")
        return
    
    historial = []
    
    # Resto del código...
```

### Paso 5: Simplifica el menú principal (DESAFÍO)
Este es el cambio más complejo. Actualmente tenemos:

```python
while True:
    mostrar_menu()
    opcion = input("\nElige una opción: ")
    
    if opcion == "7":
        # guardar y salir
        break
    
    # ... resto del código
```

**Desafío**: ¿Puedes usar el operador morsa para capturar la opción directamente en el `while`?

**Pista**: Piensa en combinar `mostrar_menu()` y el `input()` en una sola expresión.

### Paso 6: Prueba tu refactorización

Ejecuta el programa y verifica que:
- ✅ El menú funciona igual que antes
- ✅ Las validaciones siguen funcionando
- ✅ El historial se guarda y carga correctamente
- ✅ La opción "limpiar historial" funciona

---

## 🎯 Resultado esperado

Tu calculadora v7 debe:
- ✅ Tener menos líneas de código que la v6
- ✅ Funcionar exactamente igual (mismo comportamiento)
- ✅ Ser más legible en las validaciones
- ✅ Usar el operador morsa en **al menos 3 lugares**

---

## 🚨 Errores comunes

### ❌ Error 1: Olvidar paréntesis
```python
# ❌ SyntaxError
if opcion := input("Opción: ") == "7":
    
# ✅ Correcto
if (opcion := input("Opción: ")) == "7":
```

### ❌ Error 2: Abusar del operador (código ilegible)
```python
# ❌ Difícil de leer
if (n1 := float(i1 := input("Num: "))) > 0 and (n2 := float(i2 := input("Num: "))) > 0:
    
# ✅ Mejor dividir
entrada1 = input("Primer número: ")
entrada2 = input("Segundo número: ")
if (n1 := float(entrada1)) > 0 and (n2 := float(entrada2)) > 0:
```

### ❌ Error 3: Usar operador morsa donde no aporta valor
```python
# ❌ No mejora nada
if (resultado := sumar(a, b)):
    print(resultado)

# ✅ Más claro sin operador morsa
resultado = sumar(a, b)
print(resultado)
```

---

## 💡 Bonus: Extensiones opcionales

Si terminas rápido y quieres practicar más:

### 1️⃣ Refactoriza la carga del historial
```python
def cargar_historial():
    try:
        with open(ARCHIVO_HISTORIAL, "r") as archivo:
            datos = json.load(archivo)
            print(f"✅ Historial cargado: {len(datos)} operaciones")
            return datos
    except FileNotFoundError:
        print("📝 No hay historial previo")
        return []
```

**Desafío**: Usa operador morsa para evitar repetir `json.load(archivo)`.

### 2️⃣ Validación de número con operador morsa
```python
while True:
    entrada = input("Número: ")
    try:
        numero = float(entrada)
        break
    except ValueError:
        print("❌ Número inválido")
```

**Desafío**: Refactoriza para que la validación esté en una sola línea.

---

## 🏁 Checklist final

Antes de dar por terminado el ejercicio:

- [ ] He leído el cheat sheet del operador morsa
- [ ] He refactorizado al menos 3 lugares con operador morsa
- [ ] El programa funciona igual que la v6
- [ ] He probado todas las opciones del menú
- [ ] He verificado que el historial se guarda y carga correctamente
- [ ] He comprobado que el código es más legible (no más confuso)
- [ ] He añadido comentarios explicando por qué usé el operador morsa

---

## 🎓 Reflexión final

El operador morsa es una herramienta **poderosa pero peligrosa**. Úsalo cuando:
- ✅ Elimina repetición de código
- ✅ Mejora la legibilidad
- ✅ Hace el código más expresivo

**No lo uses** cuando:
- ❌ Hace el código más difícil de entender
- ❌ Lo usas solo porque "es moderno"
- ❌ Necesitas compatibilidad con Python < 3.8

---

## 📚 Recursos adicionales

- [`cheatsheets/07_operador_morsa.md`](../../cheatsheets/07_operador_morsa.md) - Guía completa
- [PEP 572](https://www.python.org/dev/peps/pep-0572/) - Especificación oficial
- [Real Python - Walrus Operator](https://realpython.com/python-walrus-operator/) - Tutorial detallado

---

**¡Éxito con tu refactorización!** 🦭✨
