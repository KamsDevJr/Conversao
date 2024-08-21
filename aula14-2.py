from random import randint

tentativas = 0
pc = (randint(0, 10))
jogador = int(input("Qual número eu pensei?"))
comp = print("O computador pensou em {}".format(pc))
while jogador != pc:
    jogador = int(input("Qual número eu pensei? Ainda não é esse: "))
    comp = print("O computador pensou em {}".format(pc))
    tentativas = tentativas + 1
else: jogador == pc
print("Parábens você acertou com {} tentativas".format(tentativas))
