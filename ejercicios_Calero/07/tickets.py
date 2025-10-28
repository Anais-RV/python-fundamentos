import json
import os

def cargar_tickets(fichero="tickets.json"):
    if os.path.exists(fichero):
        with open(fichero, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_tickets(tickets, fichero="tickets.json"):
    with open(fichero, "w", encoding="utf-8") as f:
        json.dump(tickets, f, ensure_ascii=False, indent=2)

def generar_nuevo_id(tickets):
    if not tickets:
        return 1
    ids = [t["id"] for t in tickets]
    return max(ids) + 1

def crear_ticket(tickets):
    titulo = input("Título del ticket: ")
    nuevo = {
        "id": generar_nuevo_id(tickets),
        "titulo": titulo,
        "estado": "abierto"
    }
    tickets.append(nuevo)
    print(f"Ticket creado con id {nuevo['id']}")

def listar_tickets(tickets):
    if not tickets:
        print("No hay tickets.")
        return
    for t in tickets:
        print(f"[{t['id']}] {t['titulo']} - {t['estado']}")

def cerrar_ticket(tickets):
    try:
        tid = int(input("ID del ticket a cerrar: "))
    except ValueError:
        print("ID inválido.")
        return
    for t in tickets:
        if t["id"] == tid:
            t["estado"] = "cerrado"
            print(f"🔒 Ticket {tid} cerrado.")
            return
    print("No existe ese ID.")

def menu_tickets():
    tickets = cargar_tickets()

    while True:
        print("\n=== TICKETS ===")
        print("1) Crear ticket")
        print("2) Listar tickets")
        print("3) Cerrar ticket")
        print("4) Salir")
        opcion = input("> ")

        if opcion == "1":
            crear_ticket(tickets)
        elif opcion == "2":
            listar_tickets(tickets)
        elif opcion == "3":
            cerrar_ticket(tickets)
        elif opcion == "4":
            guardar_tickets(tickets)
            print("Guardado. See you!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_tickets()
