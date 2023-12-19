
idades = []
pessoasMenor = 0
pessoasMaior = 0
contador = 0

while contador < 10:
    contador += 1
    idade = int(input("digite sua idade: "))
    idades.append(idade)
    if idade > 18:
         pessoasMaior = pessoasMaior + 1
    elif idade <= 5:
         pessoasMenor = pessoasMenor +1


soma = sum(idades)
media = soma/len(idades)
maiorIdade = max(idades)

print(f"A idade média do grupo é de {media}")
print(f"Pessoa com +18 anos {pessoasMaior}")
print(f"Pessoas com -5 anos {pessoasMenor}")
print(f"A maior idade lida foi {maiorIdade}")
