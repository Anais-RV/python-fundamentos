# 🎯 La Calculadora que Crece - Versión 4

¡Hora de la gran refactorización! En esta versión organizarás todo tu código en funciones reutilizables, siguiendo las mejores prácticas de programación.

## 🎓 Qué aprenderás

En este módulo estamos aprendiendo:
- ✅ Definir funciones con `def`
- ✅ Parámetros y valores de retorno
- ✅ Docstrings para documentar código
- ✅ Organización modular del código
- ✅ Patrón `if __name__ == "__main__"`

## 🎯 Objetivo de la v4

Refactorizar la calculadora para que:
1. Cada operación sea una función separada
2. El menú esté en su propia función
3. La lógica principal esté en una función `main()`
4. Cada función tenga su docstring
5. El código sea más fácil de leer, probar y mantener

**Estructura del código:**
```python
def sumar(a, b):
    """Suma dos números."""
    return a + b

def mostrar_menu():
    """Muestra el menú de opciones."""
    # ...

def obtener_numeros():
    """Pide dos números al usuario."""
    # ...

def main():
    """Función principal."""
    while True:
        # Lógica del programa

if __name__ == "__main__":
    main()
```

## 📝 Instrucciones

1. Abre el archivo `calculadora_v4.py`
2. Encontrarás la estructura base con TODOs
3. Completa cada función siguiendo las instrucciones
4. Nota cómo el código es más limpio y organizado

## ✅ Cómo probar tu código

Ejecuta el programa:
```powershell
python calculadora_v4.py
```

La funcionalidad debe ser idéntica a la v3, pero el código está mucho mejor organizado.

## 🆚 Cambios respecto a la v3

| Aspecto | v3 | v4 |
|---------|----|----|
| Organización | Todo en secuencia | Funciones modulares |
| Operaciones | Código repetido | Funciones `sumar()`, `restar()`, etc. |
| Menú | Mezclado con lógica | Función `mostrar_menu()` |
| Lectura números | Repetido | Función `obtener_numeros()` |
| Documentación | Comentarios sueltos | Docstrings en cada función |
| Reutilización | Difícil | Fácil importar y usar |

## 🚀 ¿Terminaste?

¡Perfecto! Has dado un gran paso hacia código profesional:
```bash
git add 04_funciones/ejercicio_guiado/calculadora_v4.py
git commit -m "refactor: calculadora v4 - código modular con funciones"
```

En el módulo 05 añadirás un historial de operaciones usando listas y diccionarios.

## 💡 Tips

- Las funciones deben hacer **una sola cosa** (principio de responsabilidad única)
- Usa `return` para devolver valores desde las funciones
- Los docstrings van justo después de la definición de la función, entre `"""`
- `if __name__ == "__main__":` permite que el archivo sea importable sin ejecutarse automáticamente

## 📚 Recursos

- Consulta [`cheatsheets/04_funciones.md`](../../cheatsheets/04_funciones.md) para funciones
- Revisa ejemplos de funciones con parámetros y return

---

**Versión anterior**: [`03_control_flujo/ejercicio_guiado/GUIA.md`](../../03_control_flujo/ejercicio_guiado/GUIA.md)  
**Siguiente versión**: [`05_colecciones/ejercicio_guiado/GUIA.md`](../../05_colecciones/ejercicio_guiado/GUIA.md) - Añadirás historial de operaciones