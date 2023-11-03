from datetime import datetime

ano_nascimento = int(input("digite seu ano de nascimento"))

ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

if idade < 18:
    anos_faltantes = 18 - idade
    print(f"você ainda não tem idade para se alistar, restam {anos_faltantes} anos para o alistamento.")
elif idade == 18:
    print(f"você pode se alistar esse ano!")
else:
    anos_passados = idade - 18
    print(f"já se passou {anos_passados} anos do seu alistamento ")
