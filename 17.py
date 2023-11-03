# Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h, exiba uma mensagem dizendo
# que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por cada km acima da velocidade permitida.

velo = int(input())

if velo > 80:
    dif = velo - 80
    valor = dif*5
    print("você sera multado")
    print("valor da multa R$:",valor)

else:
    print("você não estava acima do limite de velocidade.")