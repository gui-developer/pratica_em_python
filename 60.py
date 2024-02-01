#60) Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas.
#O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
#a) O nome da pessoa mais velha
#b) O nome da mulher mais jovem
#c) A média de idade do grupo
# Inicialize as listas
nomesHomens = []
idadesHomens = []
nomesMulheres = []
idadesMulheres = []

maisdetrinta = 0
menordeidade = 0

while True:
    sexo = input("Digite seu sexo (F ou M): ").upper()

    if sexo == "M":
        nome = input("Digite seu nome: ")
        nomesHomens.append(nome)
        idade = int(input("Digite sua idade: "))
        idadesHomens.append(idade)
        if idade >= 30:
            maisdetrinta += 1

    elif sexo == "F":
        nome = input("Digite seu nome: ")
        nomesMulheres.append(nome)
        idade = int(input("Digite sua idade: "))
        idadesMulheres.append(idade)
        if idade <= 18:
            menordeidade += 1

    continuar = input("Deseja continuar? (S para sim, qualquer outra coisa para não): ").upper()
    if continuar != "S":
        break

# Juntando os arrays
todos_os_nomes = nomesMulheres + nomesHomens
todas_as_idades = idadesMulheres + idadesHomens

# Calculando a média de idade do grupo
media = sum(todas_as_idades) / len(todas_as_idades)

# Descobrindo quem tem a maior idade
maior_idade = max(todas_as_idades)
indice_maior_idade = todas_as_idades.index(maior_idade)
nome_maior_idade = todos_os_nomes[indice_maior_idade]

# Descobrindo quem tem a menor idade
mulher_mais_nova = min(todas_as_idades)
indice_menor_idade = todas_as_idades.index(mulher_mais_nova)
nome_mulher_mais_nova = todos_os_nomes[indice_menor_idade]

print(f"O nome da pessoa mais velha é {nome_maior_idade}")
print(f"O nome da mulher mais nova é {nome_mulher_mais_nova}")
print(f"Número de homens com 30 anos ou mais: {maisdetrinta}")
print(f"Número de mulheres com 18 anos ou menos: {menordeidade}")
print(f"Média de idade do grupo: {media:.2f}")
