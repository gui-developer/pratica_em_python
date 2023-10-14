#Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.

print("digite uma distancia em metros : ")
valor = float(input())
print("km = ",valor/1000.0)
print("hm = ",valor/100)
print("dam = ",valor/10)
print("da = ", valor*10)
print("cm = ", valor*100)
print("mm = ", valor*1000)
