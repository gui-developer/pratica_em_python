
x = int(input("digite o valor de x"))
y = int(input("digite o valor de y"))
z = int(input("digite o valor de z"))

if x < y + z or y < x + z or z < x+y:
    print("trata-se de um triangulo")

elif x == y or x == z:
    print("Três lados iguais.")
elif x == y or x == z:
    print("Dois lados iguais.")
else:
    print("Três lados diferentes.")