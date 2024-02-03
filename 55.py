#
import random

pc = random.randint(1, 10)
contador = 0

while contador < 4:
    num = int(input("digite um numero "))
    if num == pc:
        print("você acertou o numero ")
    else:
        print("você errou, tente novamente")

    contador += 1
