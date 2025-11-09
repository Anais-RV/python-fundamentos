import csv
import os

# ------------------------------
# Mini Sistema de Tickets
# ------------------------------

TICKETS = []  # Lista principal: cada ticket será un diccionario

# define la función que carga tickets desde el CSV por defecto tickets.csv. archivo es el nombre/ruta del fichero.
def cargar_tickets(archivo="tickets.csv"):
    
    if not os.path.exists(archivo): # comprueba si el archivo no existe.
        return # si no existe el archivo, sale de la función (no hace nada).
    
    # abre el archivo en modo lectura, asegura cierre automático, newline='' es la práctica recomendada con csv y se usa utf-8.
    with open(archivo, newline='', encoding="utf-8") as f:

        #crea un lector que devuelve cada fila como diccionario usando la primera fila del CSV como nombres de columna (id, titulo, estado).
        reader = csv.DictReader(f)
        for row in reader: # itera por cada fila/diccionario leído.

            # añade a la lista global TICKETS un diccionario con:
            # "id": int(row["id"]) — convierte el campo id del CSV a entero.
            # "titulo": row["titulo"] — título tal cual.
            # "estado": row["estado"] — estado tal cual (por ejemplo "abierto" o "cerrado").
            TICKETS.append({
                "id": int(row["id"]),
                "titulo": row["titulo"],
                "estado": row["estado"]
            })

# define la función para escribir los tickets en archivo.
def guardar_tickets(archivo="tickets.csv"):
    
    with open(archivo, "w", newline='', encoding="utf-8") as f: # abre/crea el archivo en modo escritura (sobrescribe si ya existe).
        fieldnames = ["id", "titulo", "estado"] # lista de columnas para el CSV.
        writer = csv.DictWriter(f, fieldnames=fieldnames) # crea un escritor que acepta diccionarios con esas claves.
        writer.writeheader() # escribe la fila de cabecera (id,titulo,estado).
        for t in TICKETS: # itera cada ticket en la lista global.
            writer.writerow(t) # escribe la fila correspondiente al diccionario t.

# función que recibe un titulo para el ticket.
def crear_ticket(titulo):
    
     # Obtener el ID más alto existente o 0 si no hay tickets
    # (t["id"] for t in TICKETS) → es una expresión generadora que recorre todos los tickets y extrae sus IDs.
    # max(..., default=0) → obtiene el máximo ID actual. Si TICKETS está vacío, usa default=0 para evitar error y empezar desde 1.
    # Luego le sumamos +1 para crear el nuevo ID.
    nuevo_id = max((t["id"] for t in TICKETS), default=0) + 1
    ticket = {"id": nuevo_id, "titulo": titulo, "estado": "abierto"} # crea el diccionario del ticket con estado inicial "abierto".
    TICKETS.append(ticket) # añade el ticket a la lista global.
    print(f"✅ Ticket creado: #{nuevo_id} - '{titulo}'") # confirma por consola que se creó el ticket mostrando su id y título.


def listar_tickets(): # función que imprime la lista de tickets por consola.
   
    if not TICKETS: # si la lista está vacía:
        print("⚠️ No hay tickets registrados.")
        return

    print("\n🎟️  Lista de tickets:") 
    print("-" * 35) # línea separadora (35 guiones).
    for t in TICKETS: # itera todos los tickets.
        print(f"#{t['id']:03d} | {t['titulo']:<20} | Estado: {t['estado']}") # imprime cada ticket con formato: 
        # #{t['id']:03d} → id con 3 dígitos, relleno con ceros (p. ej. #001).
        # {t['titulo']:<20} → título alineado a la izquierda en campo de 20 caracteres.
        # Estado: {t['estado']} → imprime el estado.
    print("-" * 35)


def cerrar_ticket(ticket_id): # cierra (marca como "cerrado") un ticket por su id.
    """Cierra un ticket según su ID."""
    for t in TICKETS:
        if t["id"] == ticket_id: # si encuentra el ticket con el id buscado:
            if t["estado"] == "cerrado": # si ya estaba cerrado: imprime advertencia y return (sale).
                print(f"⚠️ El ticket #{ticket_id} ya estaba cerrado.")
                return
            t["estado"] = "cerrado" # cambia el estado a "cerrado".
            print(f"✅ Ticket #{ticket_id} cerrado correctamente.")
            return
    print(f"❌ No se encontró el ticket con ID {ticket_id}.")


# ------------------------------
# Ejemplo de uso interactivo
# ------------------------------

def menu():
    cargar_tickets()  # al iniciar el menú, intenta cargar tickets desde tickets.csv (si existe).

    while True:
        print("\n--- 🎫 Sistema de Tickets ---")
        print("1. Crear ticket")
        print("2. Listar tickets")
        print("3. Cerrar ticket")
        print("4. Guardar y salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título del ticket: ")
            crear_ticket(titulo)

        elif opcion == "2":
            listar_tickets()

        elif opcion == "3":
            try:
                ticket_id = int(input("ID del ticket a cerrar: "))
                cerrar_ticket(ticket_id)
            except ValueError:
                print("⚠️ ID inválido.")

        elif opcion == "4":
            guardar_tickets()
            print("💾 Datos guardados. ¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida, intenta de nuevo.")


# Ejecutar el menú solo si el archivo se ejecuta directamente
if __name__ == "__main__":
    menu()
