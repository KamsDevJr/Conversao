sal = float(input("Qual o valor de seu salário?"))
if sal >= 1.250:
    print('O seu aumento de 10% equivale a {}'.format(sal /10+sal))
else:
    print("Seu salário deve ter um aumento de 15%, o que equivale a {}".format(sal /15+sal))
