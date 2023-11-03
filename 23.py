nome = input("digite seu nome ")
print("digite seu sexo Masculino ou Feminino")
sexo = input("")
valorCompra = float(input("qual foi o valor da sua compra ?"))

if sexo == "Feminino":
    valorfinal = valorCompra - valorCompra * 0.13
    print(f"sua compra com 13% de desconto ficou no valor de R$:{valorfinal}")
else:
    valorfinal = valorCompra - valorCompra * 0.05
    print(f"sua compra com 5% de desconto ficou no valor de R$:{valorfinal}")
