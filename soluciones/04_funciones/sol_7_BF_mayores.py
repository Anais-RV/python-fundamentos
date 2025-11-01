gatos = [
    {"nombre": "Garfield", "edad": 3},
    {"nombre": "Luna", "edad": 7},
    {"nombre": "Bagira", "edad": 5},
    {"nombre": "Nina", "edad": 8}
]

def gatos_mayores(gatos: list[dict]) -> list[dict]:
    if not isinstance(gatos, list):
        raise TypeError("Se esperaba una lista de gatos")
    return [g for g in gatos if isinstance(g, dict) and g.get("edad", 0) > 5]

print(gatos_mayores(gatos))