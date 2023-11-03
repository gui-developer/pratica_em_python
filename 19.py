# Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
# média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
# não um bom aproveitamento (se ficou acima da média 7.0)

notaUm = float(input())
notaDois = float(input())

media = (notaUm+notaDois)/2

if media >= 7.0:
    print("parabens, ficou acima da média",media)
else:
    print("não teve um bom aproveitamento")
