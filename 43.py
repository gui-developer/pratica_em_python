contador = 30

while contador > 0:
    contador -=1
    if contador % 4 == 0:
        print(f"[{contador}]")
    else:
        print(f"{contador}")
