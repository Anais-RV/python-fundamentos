# 🎯 La Calculadora que Crece - Versión 6 (Final)

¡La versión final! En esta última versión añadirás persistencia: el historial se guardará en un archivo JSON para que no se pierda al cerrar el programa.

## 🎓 Qué aprenderás

En este módulo estamos aprendiendo:
- ✅ Lectura y escritura de archivos
- ✅ Formato JSON
- ✅ Manejo de excepciones (FileNotFoundError, JSONDecodeError)
- ✅ Persistencia de datos
- ✅ Módulo `json` de Python

## 🎯 Objetivo de la v6

Añadir persistencia a tu calculadora para que:
1. Al iniciar, cargue el historial desde un archivo JSON (si existe)
2. Al salir, guarde el historial en el archivo JSON
3. Opción adicional: Limpiar historial
4. El historial persiste entre sesiones

**Ejemplo de ejecución:**
```
🔄 Cargando historial...
✅ Historial cargado: 3 operaciones

=== CALCULADORA ===
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Ver historial
6. Limpiar historial
7. Salir

(realizas operaciones...)

Elige una opción: 7
💾 Guardando historial...
✅ Historial guardado correctamente
¡Hasta pronto! 👋
```

Al volver a ejecutar:
```
🔄 Cargando historial...
✅ Historial cargado: 5 operaciones
```

¡El historial se mantuvo!

## 📝 Instrucciones

1. Abre el archivo `calculadora_v6.py`
2. Encontrarás nuevas funciones para cargar y guardar
3. Completa las funciones de persistencia
4. Actualiza main() para cargar al inicio y guardar al salir

## ✅ Cómo probar tu código

Ejecuta el programa:
```powershell
python calculadora_v6.py
```

Casos de prueba:
- ✅ Primera ejecución: No hay historial → se crea vacío
- ✅ Realiza 3-4 operaciones
- ✅ Sal del programa (opción 7)
- ✅ Vuelve a ejecutar → el historial debe estar ahí
- ✅ Usa "Limpiar historial" → debe borrar el archivo y vaciar la lista
- ✅ Verifica que se creó `historial_calculadora.json` en la misma carpeta

## 🆚 Cambios respecto a la v5

| Aspecto | v5 | v6 |
|---------|----|----|
| Persistencia | Se pierde al salir | Se guarda en archivo JSON |
| Al iniciar | Historial vacío | Carga historial previo |
| Al salir | Historial se pierde | Guarda automáticamente |
| Limpieza | No disponible | Opción "Limpiar historial" |
| Archivo | No usa archivos | `historial_calculadora.json` |
| Menú | 6 opciones | 7 opciones |

## 🚀 ¿Terminaste?

¡**FELICIDADES**! Has completado toda la serie de la calculadora:
```bash
git add 06_archivos_y_modulos/ejercicio_guiado/calculadora_v6.py
git commit -m "feat: calculadora v6 - persistencia con JSON (versión final)"
```

### 🎉 Lo que has logrado

Has construido una calculadora completa que:
- ✅ Realiza las 4 operaciones básicas
- ✅ Tiene un menú interactivo con validación
- ✅ Está organizada en funciones modulares
- ✅ Guarda historial de operaciones
- ✅ Persiste datos entre sesiones con JSON
- ✅ Maneja errores correctamente

**Has aplicado**:
- Variables, tipos, input/output (Módulo 01)
- Operadores, f-strings (Módulo 02)
- Condicionales, bucles, validación (Módulo 03)
- Funciones, modularidad (Módulo 04)
- Listas, diccionarios (Módulo 05)
- Archivos, JSON, excepciones (Módulo 06)

## 💡 Tips

- Usa `json.load()` para leer JSON y `json.dump()` para escribir
- Parámetro `indent=2` hace el JSON más legible
- `ensure_ascii=False` permite caracteres especiales (ej: emojis)
- Usa `try/except` para manejar archivo no encontrado o corrupto
- Encoding UTF-8: `open(archivo, "r", encoding="utf-8")`

## 📚 Recursos

- Consulta [`cheatsheets/06_archivos_y_modulos.md`](../../cheatsheets/06_archivos_y_modulos.md) para archivos y JSON
- Revisa ejemplos de lectura/escritura con manejo de errores

## 🎁 Bonus: Versión modular (opcional)

Si quieres ir más allá, puedes separar el código en múltiples archivos:
- `operaciones.py` - Funciones matemáticas
- `historial.py` - Gestión del historial
- `interfaz.py` - Menú y entrada de usuario
- `main.py` - Punto de entrada

Consulta la carpeta `calculadora_modular/` (si existe) para ver un ejemplo.

---

**Versión anterior**: [`05_colecciones/ejercicio_guiado/GUIA.md`](../../05_colecciones/ejercicio_guiado/GUIA.md)  
**¡Proyecto completado!** 🎉 Has terminado toda la serie de ejercicios guiados.
