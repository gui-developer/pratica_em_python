contador = 0
soma_idades = 0
quantidadeHomens = 0
quantidadeMulheres = 0
mediaGrupo = 0
mediaHomens = 0
mulheres_mais_de_20 = 0

while contador < 5:
    contador += 1
    idade = int(input("digite sua idade : "))
    sexo = input("digite seu sexo (F ou M)").upper()

    if sexo == 'M':
        quantidadeHomens += 1
        mediaHomens += idade

    elif sexo == 'F':
        quantidadeMulheres += 1
        if idade > 20:
            mulheres_mais_de_20 += 1

soma_idades += idade

mediaGrupo = soma_idades / 5
if quantidadeHomens > 0:
    mediaHomens /= quantidadeHomens

print(f"resultados finais: ")
print(f"quantidade de homens cadastrados:{quantidadeHomens} ")
print(f"quantidade de mulheres cadastradas:{quantidadeMulheres} ")
print(f"media de idade do grupo:{mediaGrupo}")
print(f"media de idade dos homens:{mediaHomens} ")
print(f"mulheres com mais de 20 anos:{mulheres_mais_de_20}")
