
print("pedra")
print("papel")
print("tesoura")
JogadorUm = int(input())
JogadorDois = int(input())

if JogadorUm == JogadorDois:
    print("Empate!")
elif JogadorUm == "pedra" and JogadorDois == "tesoura":
    print("Você venceu!")
elif JogadorUm == "pedra" and JogadorDois == "papel":
    print("Você perdeu!")
elif JogadorUm == "papel" and JogadorDois == "pedra":
    print("Você venceu!")
elif JogadorUm == "papel" and JogadorDois == "tesoura":
    print("Você perdeu!")
elif JogadorUm == "tesoura" and JogadorDois == "pedra":
    print("Você venceu!")
elif JogadorUm == "tesoura" and JogadorDois == "papel":
    print("Você perdeu!")
else:
    print("entrada invalidada")
