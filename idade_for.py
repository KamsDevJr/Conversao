from time import sleep
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input("Qual o ano {}° pessoa nasceu?".format(pess)))
    idade: int = atual - nasc
    if idade >= 21:
        totmaior += 1
    elif idade < 21:
        totmenor += 1
print("Analisando...")
sleep(3)
print("\33[31mAo todo tivemos {} pessoas maiores de idade".format(totmaior))
print("\33[32mE tivemos {} pessoas menores de idade".format(totmenor))