#Faça um programa que leia 7 números inteiros e no final mostre o somatório
#entre eles.

somatorio = 0
contador = 0

while contador < 7:
    numero = int(input("Digite um número inteiro: "))

    somatorio += numero

    contador += 1

print(f"O somatório dos 7 números é: {somatorio}")
