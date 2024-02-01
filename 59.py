
quantidade_Homens = 0
soma_idade_homens = 0
idadeM = []
idadeF = []
idades = []

while True:
    sexo = input(f"digite seu sexo F ou M: ").upper()

    if sexo == "M":
        quantidade_Homens += 1
        idade = int(input(f"digite sua idade: "))
        idadeM.append(idade)
        soma_idade_homens += idade

    elif sexo == "F":
        idade = int(input(f"digite sua idade: "))
        idadeF.append(idade)

    continuar = input("Deseja cadastrar outro aluno? (S para sim, N para não): ").upper()
    if continuar == "N":
        break

media_idade_homens = soma_idade_homens / quantidade_Homens if quantidade_Homens > 0 else 0
maior_idade_M = max(idadeM) if idadeM else 0
maior_idade_F = max(idadeF) if idadeF else 0
menor_idade_F = min(idadeF) if idadeF else 0

if maior_idade_M > maior_idade_F:
    print(f"A maior idade é {maior_idade_M}")
    print(f"A quantidade de homens cadastrador foi de : {quantidade_Homens}")
    print(f"A idade da mulher mais jovem foi de : {menor_idade_F}")
elif maior_idade_M < maior_idade_F:
    print(f"A maior idade é {maior_idade_F}")
    print(f"A quantidade de homens cadastrador foi de : {quantidade_Homens}")
    print(f"A idade da mulher mais jovem foi de : {menor_idade_F}")
else:
    print("As maiores idades são iguais nos dois arrays.")

