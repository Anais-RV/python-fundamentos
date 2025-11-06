# Mini-retos (60–90 minutos)

---

## 🦭 Retos con Operador Morsa

> **Importante**: Lee primero [`cheatsheets/07_operador_morsa.md`](../cheatsheets/07_operador_morsa.md)

### Reto 1: Procesador interactivo de comandos
**Tiempo**: 30-45 minutos  
**Nivel**: ⭐⭐ Intermedio

Crea un programa que procese comandos hasta que el usuario escriba "salir".

**Requisitos**:
- Usa operador morsa en el bucle `while`
- Comandos: `sumar x y`, `restar x y`, `multiplicar x y`, `dividir x y`
- Valida que los números sean correctos
- Muestra error si el comando no es válido

**Ejemplo de uso**:
```
Comando: sumar 5 3
✅ 5 + 3 = 8

Comando: dividir 10 0
❌ No se puede dividir por cero

Comando: hola
❌ Comando no válido

Comando: salir
¡Hasta pronto!
```

**Pistas**:
- `while (comando := input(...)) != "salir":`
- `comando.split()` para separar las partes
- Maneja `ValueError` si los números no son válidos

---

### Reto 2: Validador de formulario
**Tiempo**: 30-45 minutos  
**Nivel**: ⭐⭐ Intermedio

Crea un programa que pida datos de registro y los valide:
- Nombre (mínimo 3 caracteres)
- Email (debe contener @)
- Edad (debe ser número entre 18 y 100)
- Contraseña (mínimo 6 caracteres)

**Requisitos**:
- Usa operador morsa en TODAS las validaciones
- Repite la pregunta si el dato no es válido
- Muestra un resumen al final
- Guarda los datos en un archivo JSON

**Ejemplo de uso**:
```
Nombre: An
❌ El nombre debe tener al menos 3 caracteres
Nombre: Ana

Email: ana
❌ El email debe contener @
Email: ana@example.com

Edad: abc
❌ La edad debe ser un número
Edad: 15
❌ Debes tener al menos 18 años
Edad: 25

Contraseña: 123
❌ La contraseña debe tener al menos 6 caracteres
Contraseña: gato123

✅ Registro completado:
Nombre: Ana
Email: ana@example.com
Edad: 25
```

**Pistas**:
- `while not (nombre := input(...)) or len(nombre) < 3:`
- `while "@" not in (email := input(...)):`
- Usa `try-except` con operador morsa para validar edad

---

### Reto 3: Analizador de archivo línea por línea
**Tiempo**: 45-60 minutos  
**Nivel**: ⭐⭐⭐ Avanzado

Crea un programa que lea un archivo línea por línea y procese solo las que cumplan ciertos criterios.

**Requisitos**:
- Usa operador morsa en el bucle de lectura
- Filtra líneas que:
  - No estén vacías
  - No empiecen con `#` (comentarios)
  - Tengan más de 10 caracteres
- Cuenta cuántas líneas procesaste vs. cuántas ignoraste
- Guarda las líneas válidas en otro archivo

**Archivo de entrada ejemplo** (`datos.txt`):
```
# Este es un comentario
Línea válida para procesar
Corta

# Otro comentario
Esta línea también es válida y debe procesarse
```

**Ejemplo de uso**:
```
Archivo a procesar: datos.txt
✅ Procesadas: 2 líneas
⏭️  Ignoradas: 3 líneas (comentarios o vacías)
📝 Resultado guardado en: datos_procesados.txt
```

**Pistas**:
- `while (linea := archivo.readline()):`
- `if (linea_limpia := linea.strip()) and not linea_limpia.startswith("#") and len(linea_limpia) > 10:`

---

## 📚 Retos clásicos (módulos anteriores)

### Reto 4: Estadísticas del refugio de gatos
**Tiempo**: 60-90 minutos  
**Nivel**: ⭐⭐ Intermedio

- Entrada: archivo o lista de pesos y edades.
- Tareas: conteo, media, mediana simple, top-k más pesados.
- Salida: resumen por pantalla y guardado opcional a archivo.

**Bonus**: Usa operador morsa para leer el archivo línea por línea.

---

### Reto 5: Mini sistema de tickets
**Tiempo**: 60-90 minutos  
**Nivel**: ⭐⭐ Intermedio

- Usa listas y diccionarios para manejar tickets (id, título, estado).
- Operaciones: crear, listar, cerrar.
- Persistencia opcional en archivo.

**Bonus**: Usa operador morsa en el menú principal.

---

### Reto 6: Parser de logs simple
**Tiempo**: 60-90 minutos  
**Nivel**: ⭐⭐⭐ Avanzado

- Lee un archivo de logs, separa por espacio, cuenta por tipo o fecha.
- Guarda resultados en `resumen.txt`.

**Bonus**: Usa operador morsa para leer y filtrar líneas en una sola expresión.

---

## 💡 Consejos generales

### Para retos con operador morsa:
- ✅ Lee el cheat sheet ANTES de empezar
- ✅ Primero escribe el código sin operador morsa
- ✅ Luego refactoriza aplicando operador morsa donde tenga sentido
- ✅ Pregúntate: "¿Esto mejora o empeora la legibilidad?"

### Para todos los retos:
- 🧪 **Testea casos extremos**: entradas vacías, números negativos, archivos inexistentes
- 📝 **Documenta tu código**: añade docstrings y comentarios
- 🎨 **Mejora la UX**: mensajes claros, emojis, colores (opcional)
- 💾 **Maneja errores**: `try-except` para evitar crashes

---

## 🏆 Desafío extra: Combina todo

**Proyecto integrador** (2-3 horas):

Crea un **mini sistema de gestión de tareas** que combine:
- Operador morsa en menú y validaciones
- Persistencia en JSON
- Estadísticas (tareas completadas, pendientes, promedio de tiempo)
- Exportación a CSV

¡Demuestra todo lo que has aprendido desde el módulo 01!

---

**Tiempo total estimado para todos los retos**: 5-8 horas
