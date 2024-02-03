
contador = 0
a = 0
b = 0
c = 0
total_altura = 0
media = 0

while contador < 3:
    peso = float(input("digite seu peso: "))
    altura = float(input("digite sua altura: "))
    if peso < 50 and altura < 1.60:
        a += 1

    elif peso > 90:
        c += 1

    elif peso > 100 and altura > 1.90:
        b += 1

    total_altura += altura
    contador += 1

media = total_altura / 7

print(f"Quantidade de pessoas que pesam 90kg:{c}")
print(f"Quantidade de pessoas que pesam menos de 50kg e tem menos de 1,60: {a}")
print(f"Quantidade de pessoas que medem mais de 1,90 e pesam mais de 100kg: {b}")
print(f"media total de altura do grupo foi de {media:.2f}")
