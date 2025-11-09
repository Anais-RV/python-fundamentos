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

#Si se pasó lista (no es None ni vacía), se asigna directamente a datos. Esto prioriza los datos en memoria sobre leer un archivo.
    if lista:
        datos = lista

# Si lista no existe/pertenece y archivo tiene algún valor (habitualmente sí), entra en este bloque para intentar leer el CSV. 
    elif archivo:
        try:

# abre el archivo en modo lectura con codificación UTF-8 y garantiza su cierre automático al terminar. newline='' es la recomendación para trabajar con csv y evitar problemas con nuevas líneas.
            with open(archivo, newline='', encoding="utf-8") as f:

# crea un lector que interpreta cada fila del CSV como un diccionario donde las claves son los nombres de las columnas (por ejemplo 'peso' y 'edad').
                reader = csv.DictReader(f)

                # itera sobre cada fila del CSV.
                for row in reader:

                    # toma el valor de la columna 'peso' y lo convierte a float. Si el campo no es convertible a número, lanzará ValueError. Hace lo mismo para la columna 'edad'.
                    peso = float(row['peso'])
                    edad = float(row['edad'])
                    # añade la tupla (peso, edad) a la lista datos.
                    datos.append((peso, edad))

        # Si al intentar abrir el archivo se lanza FileNotFoundError (archivo no existe en la ruta indicada), captura esa excepción, imprime un mensaje de error con f-string e inmediatamente return para terminar la función sin más procesamiento.
        except FileNotFoundError:
            print(f"❌ No se encontró el archivo '{archivo}'.")
            return
        
    # si lista no se dio y archivo también es falsy (por ejemplo None o ""), entonces no hay fuente de datos válida. Se lanza un ValueError para indicar al llamador que debe proporcionar datos.
    else:
        raise ValueError("Debe proporcionar un archivo o una lista.")

# Si tras intentar obtener datos la lista datos está vacía (por ejemplo, CSV vacío o lista=[]), se imprime una advertencia y se retorna, evitando dividir por cero o calcular estadísticas sin datos.
    if not datos:
        print("⚠️ No hay datos disponibles.")
        return

    # --- Separar pesos y edades ---

    # Crea una lista pesos que contiene el primer elemento (peso) de cada tupla en datos. Es una list comprehension que desempaqueta cada tupla en p, _ (la _ es convencional para ignorar la edad aquí).
    pesos = [p for p, _ in datos]
    # Similar a la línea anterior, crea una lista edades con el segundo elemento (edad) de cada tupla.
    edades = [e for _, e in datos]

    # --- Calcular estadísticas ---

    # conteo es el número total de gatos (filas/datos), usando la longitud de la lista.
    conteo = len(datos)
    # Calcula la media aritmética de los pesos con statistics.mean.
    media_peso = statistics.mean(pesos)
    # Calcula la media aritmética de las edades.
    media_edad = statistics.mean(edades)
    # Calcula la mediana de los pesos con statistics.median.
    mediana_peso = statistics.median(pesos)
    # Calcula la mediana de las edades.
    mediana_edad = statistics.median(edades)

    ## Nota: si pesos o edades tiene datos no numéricos o está vacío, estas llamadas lanzarán excepciones; pero ya se comprobó que datos no está vacío, así que OK.

    # --- Top K más pesados ---

    # sorted(datos, key=lambda x: x[0], reverse=True) ordena datos de mayor a menor según el elemento x[0] (el peso). [:k] toma los primeros k elementos de esa lista ordenada, es decir, los k gatos más pesados. Asigna el resultado a top_k.
    top_k = sorted(datos, key=lambda x: x[0], reverse=True)[:k]

    # --- Crear resumen ---

    # Construye una lista de cadenas resumen con líneas de texto que formarán el informe final.
    # Usa f-strings para insertar variables. Ejemplo: {media_peso:.2f} formatea el número con 2 decimales.
    #  Incluye una cabecera, una línea separadora y las estadísticas calculadas.
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

# Itera sobre top_k usando enumerate para tener un índice i (empezando en 1).
# En cada iteración añade una línea al resumen con el ranking, el peso (dos decimales) y la edad (un decimal). Ejemplo: " 1. Peso: 4.50 kg | Edad: 3.0 años".
    for i, (peso, edad) in enumerate(top_k, start=1):
        resumen.append(f" {i}. Peso: {peso:.2f} kg | Edad: {edad:.1f} años")

# Concatena las líneas de resumen en un único string resumen_texto, separadas por saltos de línea \n.
    resumen_texto = "\n".join(resumen)
    print(resumen_texto)

    # --- Guardar si se solicita ---

    # Si el parámetro guardar no es None ni vacío, abre (o crea) un archivo en modo escritura con codificación UTF-8 en la ruta indicada por guardar.
    # Escribe resumen_texto en ese archivo.
    # Imprime un mensaje de confirmación indicando la ruta donde se guardó.
    if guardar:
        with open(guardar, "w", encoding="utf-8") as f:
            f.write(resumen_texto)
        print(f"\n✅ Resumen guardado en '{guardar}'")

estadisticas_gatos(archivo="gatos.csv", k=3)