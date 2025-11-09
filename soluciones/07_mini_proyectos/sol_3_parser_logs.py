import os
from collections import Counter

def parser_logs(archivo="logs.txt", modo="tipo", guardar="resumen.txt"):
    """
    Analiza un archivo de logs simple y genera un resumen.

    Parámetros:
        archivo (str): ruta al archivo de logs.
        modo (str): "tipo" para contar por tipo (INFO, ERROR, etc.)
                    "fecha" para contar por fecha (primera columna).
        guardar (str): ruta del archivo donde guardar el resumen.
    """
    if not os.path.exists(archivo):
        print(f"❌ No se encontró el archivo '{archivo}'.")
        return

    conteo = Counter()

    with open(archivo, encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split()
            if not partes:
                continue  # saltar líneas vacías

            if modo == "tipo" and len(partes) >= 3:
                tipo = partes[2]  # ejemplo: "ERROR" en "2025-11-09 10:33:22 ERROR Falló conexión"
                conteo[tipo] += 1

            elif modo == "fecha" and len(partes) >= 1:
                fecha = partes[0]  # ejemplo: "2025-11-09"
                conteo[fecha] += 1

    if not conteo:
        print("⚠️ No se encontraron datos válidos.")
        return

    # --- Crear resumen ---
    resumen_lineas = [
        f"📄 Resumen de logs ({modo})",
        "-" * 30
    ]
    for clave, cantidad in conteo.most_common():
        resumen_lineas.append(f"{clave}: {cantidad}")

    resumen_texto = "\n".join(resumen_lineas)

    print(resumen_texto)

    # --- Guardar ---
    with open(guardar, "w", encoding="utf-8") as f:
        f.write(resumen_texto)

    print(f"\n✅ Resumen guardado en '{guardar}'")


# ------------------------------
# Ejemplo de uso
# ------------------------------
if __name__ == "__main__":
    # Cambia el modo según quieras:
    #   modo="tipo"  → agrupa por tipo de log (INFO, ERROR, etc.)
    #   modo="fecha" → agrupa por fecha (primer campo)
    parser_logs(archivo="logs.txt", modo="tipo")
    # parser_logs("logs.txt", modo="fecha")
