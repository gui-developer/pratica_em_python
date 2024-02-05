numero_tabuada = int(input("digite o numero da tabuada que você deseja: "))

for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada}x {i} = {resultado}")
