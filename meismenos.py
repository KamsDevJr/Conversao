from time import sleep
num1= int(input('Insira seu primeiro número: '))
num2= int(input("Insira seu segundo número: "))
print("\33[32mAnálisando numeros...")
sleep(3)
if num1 > num2:
    print("O PRIMEIRO valor '{}' é maior que o {}...".format(num1, num2))
elif num1 < num2:
    print("O SEGUNDO valor '{}'é menor que {}!".format(num1, num2))
elif num1 == num2:
    print("\33[31mOs números são iguais, portanto não existe maior nem menor!")