from time import sleep
num = int(input("Escolha um número inteiro:"))
print("""Escolha uma base de conversão, sendo elas:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3]Converter para HEXADECIMAL""")
opç = int(input("Insira sua opção: "))
print("\33[32mAnálisando número...")
sleep(3)
if opç == 1:
    print("O número {} convertido para BINÁRIO é: {}".format(num,bin(num)[2:]))
elif opç == 2:
    print("O número {} convertido para OCTAL é: {}".format(num, oct(num)[2:]))
elif opç == 3:
    print("O número {} convertido para HEXADECIMAL é: {}".format(num, hex(num)[2:]))
else:
    print("\33[31mOpção inválida! Reinicie o programa e tente novamente.")