contador = int(input("digite o primeiro valor: "))
valor_final = int(input("digite o ultimo valor: "))
i = int(input("digite o incremento: "))

if contador < valor_final:
    while contador < valor_final:
        print(f"contagem:{contador}")
        contador += i
else:
    while contador > valor_final:
        print(f"contagem:{contador}")
        contador -= i



