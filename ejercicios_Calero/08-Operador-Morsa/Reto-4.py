import json

def reto4():
    archivo = input("Archivo de datos (peso edad por línea): ").strip()
    datos = []

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            while (linea := f.readline()):
                if (partes := linea.strip().split()) and len(partes) == 2:
                    try:
                        peso, edad = float(partes[0]), int(partes[1])
                        datos.append((peso, edad))
                    except ValueError:
                        continue

        if not datos:
            print("No se encontraron datos válidos")
            return

        total = len(datos)
        pesos = [p for p, _ in datos]
        edades = [e for _, e in datos]

        media_peso = sum(pesos) / total
        media_edad = sum(edades) / total

        pesos_ordenados = sorted(pesos)
        edades_ordenadas = sorted(edades)

        mediana_peso = pesos_ordenados[total // 2] if total % 2 == 1 else (pesos_ordenados[total // 2 - 1] + pesos_ordenados[total // 2]) / 2
        mediana_edad = edades_ordenados[total // 2] if total % 2 == 1 else (edades_ordenados[total // 2 - 1] + edades_ordenados[total // 2]) / 2

        k = 3
        top_k = sorted(datos, key=lambda x: x[0], reverse=True)[:k]

        print(f"Total de gatos: {total}")
        print(f"Peso medio: {media_peso:.2f}")
        print(f"Edad media: {media_edad:.2f}")
        print(f"Mediana de peso: {mediana_peso:.2f}")
        print(f"Mediana de edad: {mediana_edad:.2f}")
        print(f"Top {k} más pesados:")
        for i, (peso, edad) in enumerate(top_k, 1):
            print(f"{i}. Peso: {peso:.2f}, Edad: {edad}")

        guardar = input("¿Guardar resumen en archivo? (s/n): ").strip().lower()
        if guardar == "s":
            resumen = {
                "total": total,
                "peso_medio": media_peso,
                "edad_medio": media_edad,
                "mediana_peso": mediana_peso,
                "mediana_edad": mediana_edad,
                "top_k_pesados": top_k
            }
            with open("resumen_gatos.json", "w", encoding="utf-8") as out:
                json.dump(resumen, out, indent=2, ensure_ascii=False)
            print("Resumen guardado en resumen_gatos.json")

    except FileNotFoundError:
        print("Archivo no encontrado")