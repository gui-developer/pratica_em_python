horas_atividades = int(input("digite a quantidade de horas :"))
if horas_atividades < 10:
    pontos = horas_atividades*2
elif horas_atividades < 20:
    pontos = horas_atividades*5
else:
    pontos = horas_atividades*10

valor = pontos*0.05
print(f"R$:{valor}")

