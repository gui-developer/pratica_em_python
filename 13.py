# Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.

print("digite o valor do salário")
salario = float(input())

reajuste = salario*15/100
novoSalario = salario + reajuste

print("O novo salario com reajuste de 15% fica em ", novoSalario)
