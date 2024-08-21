from time import sleep
nota1 = float(input("Insira a sua primeira nota: "))
nota2 = float(input("Insira sua segunda nota: "))
media = (nota1 + nota2) / 2
print("Analisando sua média...")
print("Sua média é de {}.".format(media))
sleep(3)
if media < 5:
    print("\33[31mVocê está REPROVADO!")
elif media == 7 > media >= 5:
    print("\33[33mVocê foi aprovado, porém está de RECUPERAÇÃO!")
elif media >= 7.0:
    print("\33[32mVocê está APROVADO, parabéns.")
