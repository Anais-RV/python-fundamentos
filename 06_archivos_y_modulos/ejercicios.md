# Ejercicios 06_archivos_y_modulos

Tiempo estimado: 4–5h

## Guiado 1: Escribir archivo
Crea `escribir.txt` con tres líneas.

## Guiado 2: Leer archivo
Lee `escribir.txt` e imprime las líneas numeradas.

## Autónomos
1. Guarda un resumen de gatos en `gatos.csv` (separado por comas).
2. Crea un módulo `utiles.py` con `leer_lineas(ruta)` y `guardar_lineas(ruta, lineas)`.
3. Usa `utiles` desde otro script `app.py`.
4. Maneja `FileNotFoundError` de forma amable.
 5. Pide por `input()` una ruta de archivo y valida si existe antes de leer.

## Desafío: Bigotes Felices (logs)
Dado un archivo de logs `visitas.log`, cuenta por día cuántas visitas hubo y guarda un resumen.

Errores comunes: rutas relativas mal usadas, no cerrar archivos (usa `with`).

Tiempo estimado: 4–5h
