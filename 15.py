#Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário,
# sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada.

dias = float(input())
horasExtra = float(input())

valorDias = dias*200
horasExtra = horasExtra*25

salariofinal = valorDias+horasExtra
print("salario R$: ", salariofinal)