# Faça um algoritmo que leia um determinado ano e mostre se ele é ou não BISSEXTO

ano = int(input("digite um ano"))

if ano % 4 == 0 and ano % 100 != 0:
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto")
    