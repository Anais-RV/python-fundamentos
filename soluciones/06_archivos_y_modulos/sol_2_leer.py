with open("escribir.txt", "r", encoding="utf-8") as f:
    for i, l in enumerate(f, 1):
        print(f"{i}: {l.strip()}")
