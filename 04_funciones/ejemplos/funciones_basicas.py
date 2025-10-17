"""Funciones simples con parámetros y retorno."""

def saludar(nombre: str) -> str:
    """Retorna un saludo simple."""
    return f"Hola, {nombre}"

if __name__ == "__main__":
    print(saludar("Mundo"))
