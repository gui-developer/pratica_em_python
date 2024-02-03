numeros = []
valores_pares = 0

while True:
    numero = int(input("digite um numero: "))
    numeros.append(numero)
    if numero % 2:
        valores_pares +=1

    resp = input("deseja continuar? S ou N").upper()
    if resp != "S":
        break

qtd = len(numeros)
soma = sum(numeros)
media = soma / qtd
print(f"A soma de todos os valores foi de {soma}")
print(f"A quantidade de valores pares {valores_pares}")
print(f"A media entre todos os valores foi de : {media}")

