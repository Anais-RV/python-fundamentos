"""
Calculadora v4 - Código modular con funciones
==============================================

En esta cuarta versión refactorizarás todo el código en funciones reutilizables.
Verás cómo el código se vuelve más limpio, mantenible y profesional.

Conceptos aplicados:
- Definición de funciones con def
- Parámetros y return
- Docstrings para documentación
- Separación de responsabilidades
- Patrón if __name__ == "__main__"

Instrucciones:
1. Crea funciones para cada operación matemática
2. Crea función para mostrar el menú
3. Crea función para obtener números del usuario
4. Organiza todo en una función main()
"""

# TODO 1: Define las funciones para cada operación matemática
# Cada función debe recibir dos parámetros (a, b) y devolver el resultado

def sumar(a: float, b:float) -> float:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a y b deben ser números") 
    
    return a + b


def restar(a: float, b: float) -> float:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a y b deben ser números")
    
    return a - b


def multiplicar(a: float, b: float) -> float:
     if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a y b deben ser números")
     
     return a * b


def dividir(a: float, b: float) -> float:
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a y b deben ser números")
     
    return a / b


def mostrar_menu():
   
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    

def obtener_numeros():
    
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))
    return num1, num2
    


def main():
    

    while True:
       
        mostrar_menu()

        opcion = input("\nElige una opción: ")
       
        if opcion == "5":
            print("¡Hasta pronto! 👋")
            break
       
        if opcion not in ["1", "2", "3", "4"]:
            print("❌ Opción no válida")
            continue

        
        num1, num2 = obtener_numeros()

        
        if opcion == "4" and num2 == 0:
            print("❌ No se puede dividir por cero")
            continue

        
        if opcion == "1":
            resultado = sumar(num1, num2)
            simbolo = "+"
        elif opcion == "2":
            resultado = restar(num1, num2)
            simbolo = "-"
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
            simbolo = "*"
        elif opcion == "4":
            resultado = dividir(num1, num2)
            simbolo = "/"

        
        print(f"✅ {num1} {simbolo} {num2} = {resultado:.2f}")



# Este patrón permite que el archivo sea importable sin ejecutarse automáticamente
if __name__ == "__main__":
    main()


# ¡Excelente! Has refactorizado tu calculadora con funciones.
#
# Ventajas de esta versión:
# ✅ Cada función tiene una responsabilidad clara
# ✅ El código es reutilizable (puedes importar estas funciones en otros archivos)
# ✅ Es más fácil de leer y entender
# ✅ Es más fácil de probar (puedes testear cada función individualmente)
# ✅ Es más fácil de mantener y extender
#
# Prueba que funcione igual que la v3, pero nota cómo el código es más claro.
#
# 💡 En la v5 añadirás un historial de operaciones usando listas y diccionarios