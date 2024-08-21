
somaidade = 0
mediaidade = 0
homemvelho = 0
nomehom = ""
totmulher20 = 0
from time import sleep
for person in range(1,5):
    print("-----{}° PESSOA-----".format(person))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sex = str(input("Sexo [M/F]: "))
    somaidade = idade + somaidade
    if person == 1 and sex in "Mm":
        homemvelho = idade
        nomehom = nome
    if sex in "Mm" and idade > homemvelho:
        homemvelho = idade
        nomehom = nome
    if sex in "Ff" and idade < 20:
        totmulher20 = totmulher20 + 1
mediaidade = somaidade / 4
print("A média de idade do grupo é de {} anos.".format(mediaidade))
print("O homem mais velho tem {} e se chama {}".format(homemvelho, nomehom))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))
