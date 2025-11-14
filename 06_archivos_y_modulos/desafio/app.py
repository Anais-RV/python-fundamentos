# app.py
# EJERCICIO DESAFIO BIGOTES FELICES: LOGS
# Enunciado: Dado un archivo de logs `visitas.log`, cuenta por día cuántas visitas hubo y guarda un resumen.

print("--- 😺 BIGOTES FELICES: LOGS 😺 ---")

# Importamos las funciones necesarias del módulo logs
from logs import guardar_archivo, resumen_archivo, visita_por_dia

# Listamos dicts de registros
registro_logs = [
    {"fecha": "2024-10-11 08:11:59", "visita": "Visita desde IP 192.168.1.1"},
    {"fecha": "2024-10-11 10:30:43", "visita": "Visita desde IP 192.168.1.2"},
    {"fecha": "2024-10-11 12:41:12", "visita": "Visita desde IP 192.168.1.4"},
    {"fecha": "2024-10-11 17:30:29", "visita": "Visita desde IP 192.168.1.6"},
    {"fecha": "2024-10-12 08:10:32", "visita": "Visita desde IP 192.168.1.8"},
    {"fecha": "2024-10-12 11:11:48", "visita": "Visita desde IP 192.168.1.9"},
    {"fecha": "2024-10-12 18:21:51", "visita": "Visita desde IP 192.168.1.10"},
    {"fecha": "2024-10-13 08:04:12", "visita": "Visita desde IP 192.168.1.11"},
]

# Mostramos previo la lista de registros
print("\n--- Registro de logs que queremos almacenar ---")
for log in registro_logs:
    print(f"| {log["fecha"]} - {log["visita"]} |")

# Función que se encarga de guardar el contenido del archivo 'visitas.log'
guardar_archivo("visitas.log", registro_logs)

# Función que se encarga de leer el contenido del archivo 'visitas.log'
resumen_archivo("visitas.log")

# Función que devuelve un resumen de los días contados y el total de visitas de x días
visita_por_dia("visitas.log")