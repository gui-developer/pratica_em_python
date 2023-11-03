print("digite o ano de seu nascimento:")
nascimento = int(input())
ano = 2023 - nascimento
if ano >= 18:
    print("Você tem idade para votar")
else:
    print("Você ainda não tem idade para votar")

