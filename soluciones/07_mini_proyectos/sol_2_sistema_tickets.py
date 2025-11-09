import csv
import os

# ------------------------------
# Mini Sistema de Tickets
# ------------------------------

TICKETS = []  # Lista principal: cada ticket será un diccionario


def cargar_tickets(archivo="tickets.csv"):
    """Carga tickets desde un archivo CSV (si existe)."""
    if not os.path.exists(archivo):
        return

    with open(archivo, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            TICKETS.append({
                "id": int(row["id"]),
                "titulo": row["titulo"],
                "estado": row["estado"]
            })


def guardar_tickets(archivo="tickets.csv"):
    """Guarda los tickets actuales en un archivo CSV."""
    with open(archivo, "w", newline='', encoding="utf-8") as f:
        fieldnames = ["id", "titulo", "estado"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for t in TICKETS:
            writer.writerow(t)


def crear_ticket(titulo):
    """Crea un nuevo ticket y lo añade a la lista."""
    nuevo_id = len(TICKETS) + 1
    ticket = {"id": nuevo_id, "titulo": titulo, "estado": "abierto"}
    TICKETS.append(ticket)
    print(f"✅ Ticket creado: #{nuevo_id} - '{titulo}'")


def listar_tickets():
    """Muestra todos los tickets existentes."""
    if not TICKETS:
        print("⚠️ No hay tickets registrados.")
        return

    print("\n🎟️  Lista de tickets:")
    print("-" * 35)
    for t in TICKETS:
        print(f"#{t['id']:03d} | {t['titulo']:<20} | Estado: {t['estado']}")
    print("-" * 35)


def cerrar_ticket(ticket_id):
    """Cierra un ticket según su ID."""
    for t in TICKETS:
        if t["id"] == ticket_id:
            if t["estado"] == "cerrado":
                print(f"⚠️ El ticket #{ticket_id} ya estaba cerrado.")
                return
            t["estado"] = "cerrado"
            print(f"✅ Ticket #{ticket_id} cerrado correctamente.")
            return
    print(f"❌ No se encontró el ticket con ID {ticket_id}.")


# ------------------------------
# Ejemplo de uso interactivo
# ------------------------------

def menu():
    cargar_tickets()  # Cargar datos al iniciar

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
