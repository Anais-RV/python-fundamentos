# 🎯 La Calculadora que Crece - Versión 5

¡Tu calculadora ahora tiene memoria! En esta versión añadirás un historial de operaciones usando listas y diccionarios.

## 🎓 Qué aprenderás

En este módulo estamos aprendiendo:
- ✅ Listas para almacenar datos
- ✅ Diccionarios para estructurar información
- ✅ Métodos append(), enumerate()
- ✅ Iteración sobre colecciones
- ✅ Estructuras de datos complejas

## 🎯 Objetivo de la v5

Añadir a tu calculadora:
1. Una lista que guarde todas las operaciones realizadas
2. Cada operación se guarda como un diccionario con: números, operación, resultado
3. Nueva opción en el menú: "Ver historial"
4. Mostrar el historial con formato numerado

**Ejemplo de ejecución:**
```
=== CALCULADORA ===
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Ver historial
6. Salir

Elige una opción: 1
Primer número: 5
Segundo número: 3
✅ 5.0 + 3.0 = 8.0

(realiza más operaciones...)

Elige una opción: 5

📜 HISTORIAL DE OPERACIONES:
1. 5.0 + 3.0 = 8.0
2. 10.0 - 4.0 = 6.0
3. 7.0 * 2.0 = 14.0
4. 15.0 / 3.0 = 5.0
```

## 📝 Instrucciones

1. Abre el archivo `calculadora_v5.py`
2. Encontrarás la estructura base con funciones nuevas
3. Completa las funciones de historial
4. Añade la opción 5 al menú

## ✅ Cómo probar tu código

Ejecuta el programa:
```powershell
python calculadora_v5.py
```

Casos de prueba:
- ✅ Realiza varias operaciones (al menos 4-5)
- ✅ Elige "Ver historial" → debe mostrar todas las operaciones realizadas
- ✅ Realiza más operaciones y vuelve a ver el historial → deben aparecer las nuevas
- ✅ El historial se pierde al salir (normal, lo arreglaremos en v6)

## 🆚 Cambios respecto a la v4

| Aspecto | v4 | v5 |
|---------|----|----|
| Memoria | No guarda nada | Guarda todas las operaciones |
| Historial | No tiene | Opción "Ver historial" |
| Estructura datos | Variables simples | Lista + diccionarios |
| Menú | 5 opciones | 6 opciones (añade historial) |
| Persistencia | - | En memoria (se pierde al salir) |

## 🚀 ¿Terminaste?

¡Increíble! Tu calculadora ahora recuerda todo:
```bash
git add 05_colecciones/ejercicio_guiado/calculadora_v5.py
git commit -m "feat: calculadora v5 - historial de operaciones con listas y diccionarios"
```

En el módulo 06 guardarás el historial en un archivo JSON para que persista entre sesiones.

## 💡 Tips

- Crea una lista vacía al inicio: `historial = []`
- Cada operación es un diccionario: `{"num1": 5.0, "num2": 3.0, "operacion": "+", "resultado": 8.0}`
- Usa `historial.append(operacion_dict)` para añadir operaciones
- `enumerate(historial, 1)` te da índice y valor: `for i, op in enumerate(historial, 1):`
- Verifica si la lista está vacía: `if not historial:`

## 📚 Recursos

- Consulta [`cheatsheets/05_colecciones.md`](../../cheatsheets/05_colecciones.md) para listas y diccionarios
- Revisa ejemplos de append() y enumerate()

---

**Versión anterior**: [`04_funciones/ejercicio_guiado/GUIA.md`](../../04_funciones/ejercicio_guiado/GUIA.md)  
**Siguiente versión**: [`06_archivos_y_modulos/ejercicio_guiado/GUIA.md`](../../06_archivos_y_modulos/ejercicio_guiado/GUIA.md) - Añadirás persistencia con JSON
