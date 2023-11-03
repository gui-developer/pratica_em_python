#Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em Km. Calcule o preço da passagem,
# cobrando R$0.50 por Km para viagens até 200Km e R$0.45 para viagens mais longas.

Km = float(input("digite a distancia em Km "))

if Km == 200:
    Kmfinal = Km * 0.50
    print(f" o valor da sua corrida foi de R$:{Kmfinal}")
else:
    Kmfinal = Km  * 0.45
    print(f" o valor final da sua corrida foi de R$:{Kmfinal}")
