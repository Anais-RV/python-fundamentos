import json

def reto5():
    tickets = []
    siguiente_id = 1
    archivo = "tickets.json"

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            if (cargados := json.load(f)):
                tickets = cargados
                siguiente_id = max(t["id"] for t in tickets) + 1
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    while (opcion := input("\n[1] Crear [2] Listar [3] Cerrar [4] Salir\nElige: ").strip()) != "4":
        if opcion == "1":
            if (titulo := input("Título del ticket: ").strip()):
                tickets.append({"id": siguiente_id, "titulo": titulo, "estado": "abierto"})
                siguiente_id += 1
                print("Ticket creado")
            else:
                print("Título no válido")

        elif opcion == "2":
            if not tickets:
                print("No hay tickets")
            else:
                for t in tickets:
                    print(f"[{t['id']}] {t['titulo']} - {t['estado']}")

        elif opcion == "3":
            if not (id_str := input("ID del ticket a cerrar: ").strip()).isdigit():
                print("ID no válido")
                continue
            id_ticket = int(id_str)
            for t in tickets:
                if t["id"] == id_ticket:
                    t["estado"] = "cerrado"
                    print("Ticket cerrado")
                    break
            else:
                print("Ticket no encontrado")

        else:
            print("Opción no válida")

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(tickets, f, indent=2, ensure_ascii=False)
    print("Tickets guardados")