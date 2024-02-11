mulheres_cadastradas = 0
Homens = []
homens_com_mais_de_100kg = 0
pesos_mulheres = []

for i in range(1, 9):
    sexo = input("Digite seu sexo (F ou M): ").upper()
    if sexo == "F":
        mulheres_cadastradas += 1
        peso = float(input("Digite seu peso: "))
        pesos_mulheres.append(peso)
    else:
        peso = float(input("Digite seu peso: "))
        if peso > 100:
            homens_com_mais_de_100kg += 1
        Homens.append(peso)

if mulheres_cadastradas > 0:
    media_peso_mulheres = sum(pesos_mulheres) / mulheres_cadastradas
else:
    media_peso_mulheres = 0

if Homens:
    maior_peso_homem = max(Homens)
else:
    maior_peso_homem = 0

print(f"O maior peso entre os homens foi de {maior_peso_homem} kg")
print(f"A média de peso entre as mulheres é de: {media_peso_mulheres:.2f} kg")
print(f"Quantidade de homens com mais de 100 kg: {homens_com_mais_de_100kg}")
