# A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a
# quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

print("quantidade de KM")
km = float(input())

print("quantidade de dias")
dias = float(input())

valorKm = km*0.20
valorDias = dias*90
valorFinal= valorKm+valorDias

print("o preço total a pagar é de ", valorFinal)

