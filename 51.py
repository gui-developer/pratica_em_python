# Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela
# qual foi o maior e qual foi o menor preço digitados.

contador = 0
maiorvalor = 0

while contador == 8:
    preco = float(input("digite o preço do produto: R$"))
    contador += 1
    if preco > maiorvalor:
        maiorvalor = preco
    elif preco < maiorvalor:
        menorvalor = preco

print(f"maior valor foi de R$:{maiorvalor}")
print(f"menor valor foi de R$:{menorvalor}")