#Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a
# quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

print("digite a largura da parede: ")
largura = float(input())

print("digite a altura da parede: ")
altura = float(input())

area = largura*altura
tinta = area/2

print("A área a ser pintada é de ",area, " m2 e vai utilizar um total de ",tinta,"litros de tinta")