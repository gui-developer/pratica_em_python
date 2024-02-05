

mulheres_cadastradas = 0
sexos = []
Homens = []
sobrepeso = 0

for i in range(1, 8):
    sexo = input("digite seu sexo F ou M: ").upper()
    sexos.append(sexo)
    if sexo == "M":
        mulheres_cadastradas +=1
        pesoMulheres = input("digite seu peso: ")
    else:
        peso = input("digite seu peso: ")
        if peso > 100:
            sobrepeso +=1
        Homens.append(peso)


soma = sum(mulheres_cadastradas)
media = soma/len(mulheres_cadastradas)

print(f"O maior peso entre os homens foi de {max(Homens)}")
print(f"A média de peso entre as mulheres é de: {media}")