import json

def reto2():
    while not (nombre := input("Nombre: ")) or len(nombre) < 3:
        print("El nombre debe tener al menos 3 caracteres")

    while "@" not in (email := input("Email: ")):
        print("El email debe contener @")

    while True:
        try:
            if not (edad := int(input("Edad: "))) or edad < 18 or edad > 100:
                print("La edad debe estar entre 18 y 100")
                continue
            break
        except ValueError:
            print("La edad debe ser un número")

    while not (clave := input("Contraseña: ")) or len(clave) < 6:
        print("La contraseña debe tener al menos 6 caracteres")

    print("Registro completado:")
    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print(f"Edad: {edad}")

    datos = {
        "nombre": nombre,
        "email": email,
        "edad": edad,
        "contraseña": clave
    }

    with open("registro.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)