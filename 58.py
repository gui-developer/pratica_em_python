
#No final, mostre quantos alunos
#existem na turma e qual é a média de idade do grupo.

quantidadeAlunos = 0
idadetotal = 0

while True:
    idade = int(input("digite a idade de um aluno ou 999 para parar: "))
    if idade == 999:
        break
    quantidadeAlunos += 1
    idadetotal += idade

media = idadetotal/quantidadeAlunos


print(f"a quantidade de alunos : {quantidadeAlunos}")
print(f"a media de idade do grupo foi de : {media:.2f}")
