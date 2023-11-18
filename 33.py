

valor_casa = float(input("Qual o valor da casa? "))
salario_comprador = float(input("Qual o salário do comprador? "))
anos_pagamento = int(input("Em quantos anos o comprador vai pagar? "))

prestacao_mensal = valor_casa / (anos_pagamento * 12)

if prestacao_mensal > (salario_comprador * 0.3):
    print("Desculpe, o empréstimo bancário não pode ser aprovado.")
else:
    print("O empréstimo bancário pode ser aprovado.")
