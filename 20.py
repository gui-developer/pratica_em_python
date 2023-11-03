# Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR

numero = int(input())
resto = numero%2

if resto == 0:
    print("Numero par")
else:
    print("Numero impar")
