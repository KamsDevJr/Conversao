print("-"*20)
va1 = float(input("\33[37mDigite um primeiro valor:"))
va2 = float(input("\33[37mDigite um segundo valor:"))
print("-"*20)
list= ["\33[35m1-Somar","2-multiplicar","3- maior","4-novos números","5-sair do programa"]
soma = va1+va2
mult = va1*va2
for list in list:
    print(list)
op = 0
while op != 5:
    op: int = int(input("Qual opção você escolhe?"))

    if op == 1:
        print("\33[30m a soma de {} + {} é: {}".format(va1, va2, soma))

    elif op == 2:
        print("\33[32m {} multiplicado por {} é: {}".format(va1,va2,mult))

    elif op == 3:
        if va1 > va2:
            print("\33[33mO naior valor é {}".format(va1))
        else:
          print("\33[33mO maior valor é {}".format(va2))

    elif op == 4:
        va1 = float(input("Digite um primeiro valor:"))
        va2 = float(input("Digite um segundo valor:"))

print("\33[36mSair do programa")





