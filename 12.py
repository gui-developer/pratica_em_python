# Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.

print("digite o valor de um produto")
produto = float(input())

desconto = produto*5/100
aplicado = produto - desconto

print("O valor de ", produto, "com 5% de desconto fica em R$: ", aplicado)
