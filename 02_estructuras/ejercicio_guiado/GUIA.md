# 🎯 La Calculadora que Crece - Versión 2

¡Bienvenid@ de nuevo! En esta versión expandirás tu calculadora para que pueda hacer las cuatro operaciones básicas: suma, resta, multiplicación y división.

## 🎓 Qué aprenderás

En este módulo estamos aprendiendo:
- ✅ Operadores aritméticos (`+`, `-`, `*`, `/`)
- ✅ F-strings para formateo elegante
- ✅ Tipos numéricos (int vs float)
- ✅ Condicionales if/elif/else

## 🎯 Objetivo de la v2

Mejorar tu calculadora para que:
1. Pida dos números al usuario
2. Pregunte qué operación realizar (+, -, *, /)
3. Realice la operación correspondiente
4. Muestre el resultado con formato profesional usando f-strings

**Ejemplo de ejecución:**
```
Ingresa el primer número: 10
Ingresa el segundo número: 3
¿Qué operación deseas realizar? (+, -, *, /): /
El resultado de 10.0 / 3.0 = 3.33
```

## 📝 Instrucciones

1. Abre el archivo `calculadora_v2.py`
2. Encontrarás comentarios con instrucciones paso a paso
3. Completa el código siguiendo las pistas
4. Ejecuta y prueba tu programa con las 4 operaciones

## ✅ Cómo probar tu código

Ejecuta el programa:
```powershell
python calculadora_v2.py
```

Prueba cada operación:
- **Suma**: `5 + 3` → debe dar `8.0`
- **Resta**: `10 - 4` → debe dar `6.0`
- **Multiplicación**: `7 * 2` → debe dar `14.0`
- **División**: `10 / 3` → debe dar `3.33` (o similar)

## 🆚 Cambios respecto a la v1

| Aspecto | v1 | v2 |
|---------|----|----|
| Operaciones | Solo suma | 4 operaciones básicas |
| Output | `print()` simple | F-strings con formato |
| Lógica | Directa | If/elif para elegir operación |

## 🚀 ¿Terminaste?

¡Excelente! Guarda tu trabajo:
```bash
git add 02_estructuras/ejercicio_guiado/calculadora_v2.py
git commit -m "feat: completar calculadora v2 - cuatro operaciones básicas"
```

En el módulo 03 añadirás un menú interactivo que se repite hasta que el usuario decida salir.

## 💡 Tips

- Usa if/elif/else para decidir qué operación hacer
- Los f-strings te permiten interpolar variables: `f"Resultado: {resultado}"`
- Puedes formatear decimales así: `f"{numero:.2f}"` (2 decimales)
- ¿Qué pasa si divides por cero? Por ahora Python mostrará un error, lo arreglaremos en v3

## 📚 Recursos

- Consulta [`cheatsheets/02_estructuras.md`](../../cheatsheets/02_estructuras.md) para más sobre f-strings
- Revisa la sección de operadores aritméticos

---

**Versión anterior**: [`01_intro/ejercicio_guiado/GUIA.md`](../../01_intro/ejercicio_guiado/GUIA.md)  

**Siguiente versión**: [`03_control_flujo/ejercicio_guiado/GUIA.md`](../../03_control_flujo/ejercicio_guiado/GUIA.md) - Añadirás menú con bucles
