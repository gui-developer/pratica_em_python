#Crie um programa que leia o tamanho de três segmentos de reta. Analise seus comprimentos e diga se é possível
# formar um triângulo com essas retas.
# Matematicamente, para três segmentos formarem um triângulo, o comprimento de cada lado deve ser menor que a soma dos outros dois.

x = int(input("digite o valor de x"))
y = int(input("digite o valor de y"))
z = int(input("digite o valor de z"))

if x < y + z or y < x + z or z < x+y:
    print("trata-se de um triangulo")

elif x == y or x == z:
    print("Três lados iguais . Trata-se de um Triangulo Equilatero")
elif x == y or x == z:
    print("Dois lados iguais . Trata-se de um Triangulo Isosceles")
else:
    print("Três lados diferentes.")