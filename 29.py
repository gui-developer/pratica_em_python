
nome = str(input("digite o nome do funcionario "))
salario = float(input(f"digite o salario do {nome} "))
anos = int(input(f"digite quanto anos {nome} trabalhou "))

if anos >= 10:
    novoSalario = salario + salario*0.20
    print(f"{nome} teve um aumento de 20%, seu novo salario é de {novoSalario} ")
elif anos >= 3 and anos <= 10:
    novoSalario = salario + salario * 0.12
    print(f"{nome} teve um aumento de 12.5%, seu novo salario é de {novoSalario}")
else:
    print(f"{nome} trabalhou por {anos} e com isso teve um aumento de 3%")
