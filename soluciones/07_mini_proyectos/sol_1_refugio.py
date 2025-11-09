import csv
import statistics

def estadisticas_gatos(archivo="gatos.csv", lista=None, k=1, guardar=None):
    """
        
    Parámetros:
        archivo (str): ruta a un archivo CSV con columnas 'peso' y 'edad'.
        lista (list of tuples): lista [(peso, edad), ...].
        k (int): número de gatos más pesados a mostrar.
        guardar (str): ruta opcional para guardar el resumen.
    """

    # --- Cargar datos ---
    datos = []

    if lista:
        datos = lista
    elif archivo:
        try:
            with open(archivo, newline='', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    peso = float(row['peso'])
                    edad = float(row['edad'])
                    datos.append((peso, edad))
        except FileNotFoundError:
            print(f"❌ No se encontró el archivo '{archivo}'.")
            return
    else:
        raise ValueError("Debe proporcionar un archivo o una lista.")

    if not datos:
        print("⚠️ No hay datos disponibles.")
        return

    # --- Separar pesos y edades ---
    pesos = [p for p, _ in datos]
    edades = [e for _, e in datos]

    # --- Calcular estadísticas ---
    conteo = len(datos)
    media_peso = statistics.mean(pesos)
    media_edad = statistics.mean(edades)
    mediana_peso = statistics.median(pesos)
    mediana_edad = statistics.median(edades)

    # --- Top K más pesados ---
    top_k = sorted(datos, key=lambda x: x[0], reverse=True)[:k]

    # --- Crear resumen ---
    resumen = [
        "📊 Estadísticas del refugio de gatos",
        "----------------------------------",
        f"Total de gatos: {conteo}",
        f"Peso promedio: {media_peso:.2f}",
        f"Edad promedio: {media_edad:.2f}",
        f"Peso mediano: {mediana_peso:.2f}",
        f"Edad mediana: {mediana_edad:.2f}",
        "",
        f"🐾 Top {k} gatos más pesados:"
    ]

    for i, (peso, edad) in enumerate(top_k, start=1):
        resumen.append(f" {i}. Peso: {peso:.2f} kg | Edad: {edad:.1f} años")

    resumen_texto = "\n".join(resumen)
    print(resumen_texto)

    # --- Guardar si se solicita ---
    if guardar:
        with open(guardar, "w", encoding="utf-8") as f:
            f.write(resumen_texto)
        print(f"\n✅ Resumen guardado en '{guardar}'")

estadisticas_gatos(archivo="gatos.csv", k=3)