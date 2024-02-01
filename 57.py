#Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários.
#No final, mostre o total de salários pagos aos homens e o total pago às
#mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não
#sempre que ler os dados de um funcionário.

salarioHomens = 0
salarioMulheres = 0


while True:
    sexo = input("digite seu sexo F (feminino) e M (masculino) : ").upper()
    if sexo == "M":
        salario = int(input("digite seu salario : "))
        salarioHomens += salario

    elif sexo == "F":
        salario = int(input("digite seu salario : "))
        salarioMulheres += salario

    else:
        print("Por favor digite uma opção valida.")

    continuar = input("deseja continuar ? S ou N: ").upper()
    if continuar != "S":
        break

print(f"total pago as mulheres R$:{salarioMulheres}")
print(f"total pago aos homens R$:{salarioHomens}")
