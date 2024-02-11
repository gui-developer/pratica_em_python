
num_termos = 10

fibonacci = [1, 1]


for _ in range(2, num_termos):
    proximo_termo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_termo)

print("Os primeiros 10 termos da sequência de Fibonacci são:")
for termo in fibonacci:
    print(termo, end=" ")
