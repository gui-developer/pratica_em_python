
#d) qual é a média de idade entre os homens

idade = 0
idadesMulher = []
idadesHomens = []
sexo = 0
sexos = []
homens = []
mulheres = []


while True:

    sexo = input("Qual seu sexo (Digite 'F' ou 'M'): ")
    if sexo == 'M':
        homens.append(sexo)
        idade = int(input("digite sua idade"))
        idadesMulher.append(idade)
    else:
        mulheres.append(sexo)
        idade = int(input("digite sua idade"))
        idadesHomens.append(idade)


    resposta = input("Deseja continuar? (Digite 'sim' ou 'nao'): ")

    # Verifica a resposta do usuário
    if resposta.lower() != 'sim':
        break

soma = sum(idadesHomens)
quantidade = len(idadesHomens)
media = soma / quantidade

maior_numero = max(idades)
quantidade_homens = max(homens)
idade_minima = min(idadesMulher)
print(maior_numero)

