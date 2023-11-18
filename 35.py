
tipo_carro = input("Digite o tipo de carro (popular ou luxo): ")
dias = int(input("Digite a quantidade de dias de aluguel: "))
km_percorrido = int(input("Digite a quantidade de Km percorridos: "))

if tipo_carro == "popular":
        aluguel = 90 * dias
        if km_percorrido <= 100:
            custo_km = 0.20 * km_percorrido
        else:
            custo_km = 0.10 * km_percorrido
else:
        aluguel = 150 * dias
        if km_percorrido <= 200:
            custo_km = 0.30 * km_percorrido
        else:
            custo_km = 0.25 * km_percorrido

print(f"O preço a ser pago é: R$ {aluguel + custo_km}")
