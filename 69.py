
primeiro_termo = float(input("Digite o primeiro termo da PA: "))
razao = float(input("Digite a razão da PA: "))

pa = [primeiro_termo + (n - 1) * razao for n in range(1, 11)]

soma_pa = sum(pa)

print("Os 10 primeiros termos da PA são:")
for termo in pa:
    print(termo, end=" ")

print("\nA soma de todos os termos da PA é:", soma_pa)
