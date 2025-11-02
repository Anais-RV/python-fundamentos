# 🎯 La Calculadora que Crece - Versión 3

¡Tu calculadora sigue mejorando! En esta versión añadirás un menú interactivo con bucles, validación de entrada y control de errores.

## 🎓 Qué aprenderás

En este módulo estamos aprendiendo:
- ✅ Condicionales if/elif/else complejos
- ✅ Bucle while para repetir acciones
- ✅ break y continue para controlar el flujo
- ✅ Validación de entrada del usuario

## 🎯 Objetivo de la v3

Mejorar tu calculadora para que:
1. Muestre un menú numerado con las opciones
2. Permita realizar múltiples operaciones sin reiniciar el programa
3. Valide que el usuario ingrese opciones válidas
4. Controle la división por cero
5. Tenga una opción para salir

**Ejemplo de ejecución:**
```
=== CALCULADORA ===
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir

Elige una opción: 1
Primer número: 5
Segundo número: 3
✅ 5.0 + 3.0 = 8.0

=== CALCULADORA ===
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir

Elige una opción: 4
Primer número: 10
Segundo número: 0
❌ Error: No se puede dividir por cero

=== CALCULADORA ===
...
Elige una opción: 5
¡Hasta pronto! 👋
```

## 📝 Instrucciones

1. Abre el archivo `calculadora_v3.py`
2. Encontrarás comentarios con instrucciones paso a paso
3. Completa el código siguiendo las pistas
4. Ejecuta y prueba tu programa con varias operaciones seguidas

## ✅ Cómo probar tu código

Ejecuta el programa:
```powershell
python calculadora_v3.py
```

Casos de prueba:
- ✅ Realiza varias operaciones sin salir del programa
- ✅ Intenta una opción no válida (ej: 7) → debe mostrar error y volver al menú
- ✅ Intenta dividir por cero → debe mostrar error y volver al menú
- ✅ Elige opción 5 → debe salir del programa

## 🆚 Cambios respecto a la v2

| Aspecto | v2 | v3 |
|---------|----|----|
| Ejecución | Una sola operación | Múltiples operaciones |
| Menú | No tiene | Menú numerado |
| Validación | No valida | Valida opciones y división por cero |
| Bucle | No | `while True` con `break` |
| UX | Básica | Mensajes con emojis y formato |

## 🚀 ¿Terminaste?

¡Genial! Tu calculadora ahora es mucho más usable:
```bash
git add 03_control_flujo/ejercicio_guiado/calculadora_v3.py
git commit -m "feat: completar calculadora v3 - menú interactivo con validación"
```

En el módulo 04 refactorizarás todo el código en funciones para que sea más limpio y mantenible.

## 💡 Tips

- `while True:` crea un bucle infinito que solo termina con `break`
- `continue` salta al inicio del bucle sin ejecutar el resto del código
- Usa `if opcion not in ["1", "2", "3", "4", "5"]:` para validar opciones
- Para división por cero: `if num2 == 0 and opcion == "4":`

## 📚 Recursos

- Consulta [`cheatsheets/03_control_flujo.md`](../../cheatsheets/03_control_flujo.md) para bucles y control
- Revisa ejemplos de while con break/continue

---

**Versión anterior**: [`02_estructuras/ejercicio_guiado/GUIA.md`](../../02_estructuras/ejercicio_guiado/GUIA.md)  
**Siguiente versión**: [`04_funciones/ejercicio_guiado/GUIA.md`](../../04_funciones/ejercicio_guiado/GUIA.md) - Organizarás el código en funciones
