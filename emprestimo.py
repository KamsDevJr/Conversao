from time import sleep
valor = float(input("Qual o valor da casa?"))
salario = float(input("Qual o seu salário?"))
parcela = float(input("Em quantos anos você vai parcelar?"))
prestaçao = valor / (parcela*12)
limite = salario *30/ 100
print("\33[32mAnalisando dados...")
sleep(3)
print("\33[32mCalculando seu empréstimo...")
sleep(3)
print("\33[35mA sua prestação será no valor de {:.2f}$reais. \nDivididas em parcelas de {} anos...".format(prestaçao,parcela))
if prestaçao <= limite:
    print("\33[32mSeu empréstimo foi aprovado")
else:
    print("Empréstimo negado pois seu limite excede o valor do seu salário!")

