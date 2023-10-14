#Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.
print("digite o valor de A")
A = float(input())
print("digite o valor de B")
B = float(input())
print("digite o valor de C")
C = float(input())

delta = B**2 - 4*A*C

print(f"O valor de Delta (Δ) é {delta}")
