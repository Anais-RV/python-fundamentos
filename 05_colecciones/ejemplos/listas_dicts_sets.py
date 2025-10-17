"""Listas, diccionarios y sets básicos."""

gatos = ["Mishi", "Luna", "Bigotes"]
for i, nombre in enumerate(gatos, start=1):
    print(f"{i}. {nombre}")

ficha = {"nombre": "Mishi", "edad": 3}
print(f"Nombre: {ficha.get('nombre')}, Edad: {ficha.get('edad')}")

vacunas = {"rabia", "triple"}
print("rabia" in vacunas)
