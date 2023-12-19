import random

contador = 0
numeros_sorteados = []
numeros_acima_de_5 = []
numeros_divisiveis_por_3 = []

while contador < 20:
    numero_sorteado = random.randint(0, 10)
    numeros_sorteados.append(numero_sorteado)

    if numero_sorteado > 5:
        numeros_acima_de_5.append(numero_sorteado)

    if numero_sorteado % 3 == 0:
        numeros_divisiveis_por_3.append(numero_sorteado)

    contador += 1

# Exibe os resultados
print("a) Números sorteados:", numeros_sorteados)
print("b) Números acima de 5:", numeros_acima_de_5)
print("c) Números divisíveis por 3:", numeros_divisiveis_por_3)
