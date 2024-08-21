maior= 0
menor =0
#faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos
for peso in range(1,6):
    kg= float(input('Qual o peso da {}° pessoa?'.format(peso)))
    if peso == 1:
        maior = kg
        menor = kg
    else:
     if kg> maior:
            maior= kg
     if kg < menor:
                menor = kg
print("O maior peso é {}kg".format(maior))
print("O menor peso é {}kg".format(menor))