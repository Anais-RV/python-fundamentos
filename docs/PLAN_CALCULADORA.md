# 🎯 La Calculadora que Crece - Plan Maestro

Este documento describe el ejercicio guiado progresivo "La Calculadora que Crece", diseñado para aplicar los conceptos de cada módulo en un proyecto evolutivo.

## 🎓 Pedagogía del ejercicio

### Objetivos educativos

1. **Aplicación inmediata**: Los estudiantes aplican conceptos recién aprendidos
2. **Evolución visible**: Ven cómo un proyecto crece y se refactoriza
3. **Refuerzo progresivo**: Cada versión refuerza lo anterior y añade nuevo
4. **Proyecto completo**: Al final tienen una aplicación funcional real

### Filosofía de diseño

- ✅ **Incremental**: Cada versión añade UNA funcionalidad nueva
- ✅ **Práctico**: Se centra en conceptos del módulo actual
- ✅ **Guiado**: Plantillas con comentarios paso a paso
- ✅ **Opcional**: No bloquea el progreso si alguien prefiere otros ejercicios

---

## 📊 Roadmap de versiones

### v1 - Suma básica (01_intro)
**Módulo**: Introducción a Python  
**Conceptos aplicados**: Variables, input(), print(), conversión de tipos

**Funcionalidad**:
- Pide dos números al usuario
- Los suma
- Muestra el resultado

**Código clave**:
```python
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
resultado = num1 + num2
print("El resultado es:", resultado)
```

**Archivos**:
- `01_intro/ejercicio_guiado/GUIA.md`
- `01_intro/ejercicio_guiado/calculadora_v1.py`

---

### v2 - Cuatro operaciones (02_estructuras)
**Módulo**: Estructuras de datos básicas  
**Conceptos aplicados**: Operadores aritméticos, f-strings, tipos numéricos

**Funcionalidad**:
- Pide dos números
- Pide qué operación realizar (+, -, *, /)
- Realiza la operación correspondiente
- Muestra resultado formateado con f-strings

**Código clave**:
```python
operacion = input("Operación (+, -, *, /): ")
if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
# ...
print(f"El resultado de {num1} {operacion} {num2} = {resultado}")
```

**Mejoras respecto a v1**:
- ➕ Añade resta, multiplicación y división
- ➕ Usa f-strings para output más profesional
- ➕ Introduce cadenas de formato con decimales (`:.2f`)

**Archivos**:
- `02_estructuras/ejercicio_guiado/GUIA.md`
- `02_estructuras/ejercicio_guiado/calculadora_v2.py`

---

### v3 - Menú interactivo (03_control_flujo)
**Módulo**: Control de flujo  
**Conceptos aplicados**: if/elif/else, while, break/continue, validación

**Funcionalidad**:
- Menú que se repite hasta que el usuario elija salir
- Validación de entrada (operación válida, no dividir por cero)
- Manejo de errores básico

**Código clave**:
```python
while True:
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "5":
        print("¡Hasta pronto!")
        break
    
    if opcion not in ["1", "2", "3", "4"]:
        print("❌ Opción no válida")
        continue
    
    # ... pedir números y calcular
```

**Mejoras respecto a v2**:
- ➕ Menú numerado más intuitivo
- ➕ Bucle while para múltiples operaciones
- ➕ Validación de entrada del usuario
- ➕ División por cero controlada
- ➕ Opción de salir

**Archivos**:
- `03_control_flujo/ejercicio_guiado/GUIA.md`
- `03_control_flujo/ejercicio_guiado/calculadora_v3.py`

---

### v4 - Funciones modulares (04_funciones)
**Módulo**: Funciones  
**Conceptos aplicados**: Definición de funciones, parámetros, return, scope

**Funcionalidad**:
- Refactorización completa del código en funciones
- Cada operación es una función
- Menú separado en su propia función
- Código más limpio y mantenible

**Código clave**:
```python
def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta dos números."""
    return a - b

def obtener_numeros():
    """Pide dos números al usuario y los devuelve."""
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))
    return num1, num2

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    # ...

def main():
    """Función principal."""
    while True:
        mostrar_menu()
        # ...

if __name__ == "__main__":
    main()
```

**Mejoras respecto a v3**:
- ➕ Código organizado en funciones reutilizables
- ➕ Separación de responsabilidades
- ➕ Docstrings en cada función
- ➕ Patrón `if __name__ == "__main__"`
- ➕ Más fácil de testear y extender

**Archivos**:
- `04_funciones/ejercicio_guiado/GUIA.md`
- `04_funciones/ejercicio_guiado/calculadora_v4.py`

---

### v5 - Historial de operaciones (05_colecciones)
**Módulo**: Colecciones (listas, diccionarios)  
**Conceptos aplicados**: Listas, diccionarios, append, iteración

**Funcionalidad**:
- Guarda todas las operaciones realizadas en una sesión
- Opción de ver historial
- Cada operación se guarda con: números, operación, resultado

**Código clave**:
```python
historial = []

def guardar_operacion(num1, num2, operacion, resultado):
    """Guarda una operación en el historial."""
    operacion_dict = {
        "num1": num1,
        "num2": num2,
        "operacion": operacion,
        "resultado": resultado
    }
    historial.append(operacion_dict)

def mostrar_historial():
    """Muestra todas las operaciones realizadas."""
    if not historial:
        print("📭 No hay operaciones en el historial")
        return
    
    print("\n📜 HISTORIAL DE OPERACIONES:")
    for i, op in enumerate(historial, 1):
        print(f"{i}. {op['num1']} {op['operacion']} {op['num2']} = {op['resultado']}")
```

**Mejoras respecto a v4**:
- ➕ Lista para almacenar operaciones
- ➕ Diccionarios para estructurar cada operación
- ➕ Nueva opción en menú: "Ver historial"
- ➕ Uso de enumerate() para mostrar numeración
- ➕ Persistencia durante la sesión

**Archivos**:
- `05_colecciones/ejercicio_guiado/GUIA.md`
- `05_colecciones/ejercicio_guiado/calculadora_v5.py`

---

### v6 - Persistencia con archivos (06_archivos_y_modulos)
**Módulo**: Archivos y módulos  
**Conceptos aplicados**: Lectura/escritura de archivos, JSON, imports, manejo de excepciones

**Funcionalidad**:
- Guarda el historial en un archivo JSON al salir
- Carga el historial al iniciar (si existe)
- Opción de limpiar historial
- Código separado en módulos

**Código clave**:
```python
import json

ARCHIVO_HISTORIAL = "historial_calculadora.json"

def cargar_historial():
    """Carga el historial desde el archivo JSON."""
    try:
        with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("⚠️  Archivo corrupto, iniciando historial vacío")
        return []

def guardar_historial_archivo(historial):
    """Guarda el historial en el archivo JSON."""
    with open(ARCHIVO_HISTORIAL, "w", encoding="utf-8") as archivo:
        json.dump(historial, archivo, indent=2, ensure_ascii=False)
    print("✅ Historial guardado")
```

**Mejoras respecto a v5**:
- ➕ Persistencia entre sesiones con JSON
- ➕ Manejo de excepciones (archivo no existe, corrupto)
- ➕ Opción de limpiar historial
- ➕ Código separado en módulos (opcional):
  - `calculadora.py` (funciones principales)
  - `operaciones.py` (operaciones matemáticas)
  - `historial.py` (gestión de historial)
  - `main.py` (punto de entrada)

**Archivos**:
- `06_archivos_y_modulos/ejercicio_guiado/GUIA.md`
- `06_archivos_y_modulos/ejercicio_guiado/calculadora_v6.py`
- (Opcional) Versión modular en subcarpeta `calculadora_modular/`

---

## 📁 Estructura de archivos

```
python-fundamentos/
├─ 01_intro/
│  ├─ MODULO.md           ← Objetivos del módulo
│  ├─ ejercicios.md       ← Lista de ejercicios
│  └─ ejercicio_guiado/
│     ├─ GUIA.md          ← Instrucciones paso a paso
│     └─ calculadora_v1.py  ← Plantilla con TODOs
│
├─ 02_estructuras/
│  └─ ejercicio_guiado/
│     ├─ GUIA.md
│     └─ calculadora_v2.py
│
├─ 03_control_flujo/
│  └─ ejercicio_guiado/
│     ├─ GUIA.md
│     └─ calculadora_v3.py
│
├─ 04_funciones/
│  └─ ejercicio_guiado/
│     ├─ GUIA.md
│     └─ calculadora_v4.py
│
├─ 05_colecciones/
│  └─ ejercicio_guiado/
│     ├─ GUIA.md
│     └─ calculadora_v5.py
│
├─ 06_archivos_y_modulos/
│  └─ ejercicio_guiado/
│     ├─ GUIA.md
│     ├─ calculadora_v6.py
│     └─ calculadora_modular/     ← (Opcional) Versión separada en módulos
│        ├─ main.py
│        ├─ operaciones.py
│        ├─ historial.py
│        └─ calculadora.py
│
└─ docs/
   └─ PLAN_CALCULADORA.md   ← Este documento
```

---

## 🎯 Soluciones completas

**Ubicación**: Rama `solutions` → carpeta `soluciones/ejercicio_calculadora/`

Estructura en rama solutions:
```
soluciones/
└─ ejercicio_calculadora/
   ├─ calculadora_v1_solucion.py
   ├─ calculadora_v2_solucion.py
   ├─ calculadora_v3_solucion.py
   ├─ calculadora_v4_solucion.py
   ├─ calculadora_v5_solucion.py
   └─ calculadora_v6_solucion.py
```

---

## 💡 Tips pedagógicos

### Para estudiantes

- ✅ **No te saltes versiones**: Cada una refuerza la anterior
- ✅ **Prueba antes de ver la solución**: Aprende de tus errores
- ✅ **Compara tu código con la solución**: Hay muchas formas correctas
- ✅ **Es opcional**: Si prefieres otros ejercicios, está bien

### Para formadores

- ✅ **Revisa el código evolutivo**: Es fácil ver qué conceptos domina el estudiante
- ✅ **Fomenta refactorización**: Que vean cómo mejorar código previo
- ✅ **Valora diferentes enfoques**: No hay una única solución correcta
- ✅ **Usa como base para discusiones**: "¿Por qué crees que refactorizamos así?"

---

## ✅ Checklist de implementación

### Versión 1 ✅
- [x] Crear `01_intro/ejercicio_guiado/GUIA.md`
- [x] Crear `01_intro/ejercicio_guiado/calculadora_v1.py`
- [x] Actualizar `01_intro/ejercicios.md`

### Versión 2 ✅
- [x] Crear `02_estructuras/ejercicio_guiado/GUIA.md`
- [x] Crear `02_estructuras/ejercicio_guiado/calculadora_v2.py`
- [x] Actualizar `02_estructuras/ejercicios.md`

### Versión 3 ✅
- [x] Crear `03_control_flujo/ejercicio_guiado/GUIA.md`
- [x] Crear `03_control_flujo/ejercicio_guiado/calculadora_v3.py`
- [x] Actualizar `03_control_flujo/ejercicios.md`

### Versión 4 ✅
- [x] Crear `04_funciones/ejercicio_guiado/GUIA.md`
- [x] Crear `04_funciones/ejercicio_guiado/calculadora_v4.py`
- [x] Actualizar `04_funciones/ejercicios.md`

### Versión 5 ✅
- [x] Crear `05_colecciones/ejercicio_guiado/GUIA.md`
- [x] Crear `05_colecciones/ejercicio_guiado/calculadora_v5.py`
- [x] Actualizar `05_colecciones/ejercicios.md`

### Versión 6 ✅
- [x] Crear `06_archivos_y_modulos/ejercicio_guiado/GUIA.md`
- [x] Crear `06_archivos_y_modulos/ejercicio_guiado/calculadora_v6.py`
- [x] Actualizar `06_archivos_y_modulos/ejercicios.md`

### Soluciones (rama `solutions`)
- [ ] Crear soluciones completas para v1-v6 en `soluciones/ejercicio_calculadora/`

---

**Autor**: Anaïs Rodríguez Villanueva  
**Última actualización**: Octubre 2025
