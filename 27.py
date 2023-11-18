#Crie um programa que leia duas notas de um aluno e calcule a sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média até 4.9: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

notaUm = float(input("digite o valor da primeira nota "))
notaDois = float(input("digite o valor da segunda nota "))

media = (notaUm + notaDois) / 2

if media < 5.0:
    print("reprovado ")
elif media < 7.0:
    print("recuperação ")
else:
    print("aprovado ")
