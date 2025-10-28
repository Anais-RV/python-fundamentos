def calcular_media(valores):
    return sum(valores) / len(valores) if valores else 0

def calcular_mediana(valores):
    if not valores:
        return 0
    ordenados = sorted(valores)
    n = len(ordenados)
    mitad = n // 2
    if n % 2 == 1:
        return ordenados[mitad]
    else:
        return (ordenados[mitad - 1] + ordenados[mitad]) / 2

def resumen_refugio(michis, k_top=3, guardar=False, fichero_salida="resumen_refugio.txt"):
    pesos = [m["peso"] for m in michis]
    edades = [m["edad"] for m in michis]

    total = len(michis)
    peso_medio = calcular_media(pesos)
    edad_media = calcular_media(edades)
    peso_mediano = calcular_mediana(pesos)

    michis_ordenados = sorted(michis, key=lambda m: m["peso"], reverse=True)
    top_k = michis_ordenados[:k_top]

    informe = []
    informe.append(f"Total de michis: {total}")
    informe.append(f"Peso medio: {peso_medio:.2f} kg")
    informe.append(f"Peso mediano: {peso_mediano:.2f} kg")
    informe.append(f"Edad media: {edad_media:.2f} años")
    informe.append(f"Top {k_top} michis más pesados:")
    for michi in top_k:
        informe.append(f"  - {michi['nombre']}: {michi['peso']} kg ({michi['edad']} años)")
    informe_texto = "\n".join(informe)

    print(informe_texto)

    if guardar:
        with open(fichero_salida, "w", encoding="utf-8") as f:
            f.write(informe_texto)


if __name__ == "__main__":
    pass
