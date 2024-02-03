
idades = []
pessoas_com_mais_de_21 = 0

while True:
    idade = int(input("digite sua idade: "))
    idades.append(idade)
    if idade >= 21:
        pessoas_com_mais_de_21 += 1

    resp = input("deseja continuar? S ou N").upper()
    if resp != "S":
        break

qtd = len(idades)
soma = sum(idades)
media = soma / qtd
print(f"A quantidade de idades digitadas foi de:{qtd}")
print(f"A media de idades digitadas foi de {media}")
print(f"{pessoas_com_mais_de_21} tem 21 anos ou mais")
