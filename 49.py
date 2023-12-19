#Crie um programa que leia 6 números inteiros e no final mostre quantos deles são pares e quantos são ímpares.

pares = 0
impares = 0
contador = 0

while contador < 6:
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    contador += 1
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")

