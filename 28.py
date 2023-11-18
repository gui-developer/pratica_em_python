
largura = float(input("Digite a largura do terreno (em metros): "))
comprimento = float(input("Digite o comprimento do terreno (em metros): "))

area = largura * comprimento

print(f"A área do terreno é de {area}m².")
if area < 100:
    print("O terreno é classificado como TERRENO POPULAR.")
elif 100 <= area <= 500:
    print("O terreno é classificado como TERRENO MASTER.")
else:
    print("O terreno é classificado como TERRENO VIP.")