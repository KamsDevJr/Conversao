from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Vamos jogar JOkenPO
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input("Qual é a sua jogada?"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!!")
print("-=" * 12)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print('-=' * 12)
if computador == 0:  # computador jogou Pedra
    if jogador == 0:from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Vamos jogar JOkenPO
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input("Qual é a sua jogada?"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!!")
print("-=" * 12)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print('-=' * 12)
if computador == 0:  # computador jogou Pedra
    if jogador == 0:
        print("Empate!!")
    elif jogador == 1:
        print("jogador venceu.")
    elif jogador == 2:
        print("Computador venceu.")
elif computador == 1:  # computador jogou Papel
    if jogador == 0:
        print("Computador venceu.")
    elif jogador == 1:
        print("Empate!")
    elif jogador == 2:
      print("Jogador venceu!.")
elif computador == 2:  # computador jogou Tesoura
    if jogador == 0:
        print("Jogador venceu!")
    elif jogador == 1:
      print("Computador venceu!")
    elif jogador == 2:
        print("EMPATE")

        print("Empate!!")
    elif jogador == 1:
        print("jogador venceu.")
    elif jogador == 2:
        print("Computador venceu.")
elif computador == 1:  # computador jogou Papel
    if jogador == 0:
        print("Computador venceu.")
    elif jogador == 1:
        print("Empate!")
    elif jogador == 2:
      print("Jogador venceu!.")
elif computador == 2:  # computador jogou Tesoura
    if jogador == 0:
        print("Jogador venceu!")
    elif jogador == 1:
      print("Computador venceu!")
    elif jogador == 2:
        print("EMPATE")

