salario_atual = float(input("digite seu salario atual: "))
sexo = input("digite seu sexo (feminino ou masculino): ")
anos = int(input("digite quantos ano você faz parte da empresa: "))

if sexo == "feminino":
    if anos < 15:
        novosalario = salario_atual*5/100
    elif anos < 20:
        novosalario = salario_atual*12/100
    else:
        novosalario = salario_atual*23/100
else:
    if anos < 20:
        novosalario = salario_atual*3/100
    elif anos < 30:
        novosalario = salario_atual*13/100
    else:
        novosalario = salario_atual*25/100

print(novosalario + salario_atual)