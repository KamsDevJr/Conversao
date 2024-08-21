from time import sleep
from datetime import date
atual = date.today().year
nasc = int(input("Qual o ano de nascimento?"))
print("\33m Analisando dados...")
sleep(3)
idade = atual - nasc
print("\33[36Quem nasceu no ano {}: Tem {} anos no ano atual: {}".format(nasc,idade,atual))
if idade == 18:
    print("Está na hora de se alistar!!!!!")

elif idade < 18:
    saldo = 18 - idade
    print("Você ainda não tem 18 anos, portanto seu alistamento será em : {}".format(saldo))
    ano = atual+ saldo
elif idade > 18:
    saldo = idade- 18
    ano = atual - saldo
    print("\33[31mVocê precisa se alistar URGENTE, pois deveria ter feito isso no ano de {}...".format(ano))
    print("Seu alistamento foi em {}!".format(ano))