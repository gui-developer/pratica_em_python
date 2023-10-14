# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados
# por dias e quantos anos ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro.
# Calcule quantos dias de vida um fumante perderá e exiba o total em dias.

print("quantidade de cigarros fumados por dia")
quant = int(input())

print("por quantos anos você já fumou ?")
anos = int(input())

ano = 365
total = quant*ano*anos
tempo = total*10
hora = tempo/1440

print("A quantidade de dias perdidos foi de ",hora )