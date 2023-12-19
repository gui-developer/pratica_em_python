#Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 +
#450 + 400 + 350 + 300 + ... + 50 + 0

total = 0
i = 500

while i >= 0:
    total += i
    i -= 100

print(f"Soma dos números desde 500 até 0 é {total}")