from time import sleep
print("=============loja kamila==========")
preço =float(input("Qual o valor total da compra?"))
opçao = int(input('''Qual será a forma de pagamento?
[1] á vista no dinheiro/cheque
[2] á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão'''))
print("\33[32mAnálisando compra...")
sleep(3)
if opçao == 1:
    total = preço - (preço * 10/100)
    print("Sua compra ficou no valor de:{}$ com desconto de 10%".format(total))
elif opçao == 2:
    total = preço - (preço * 5/100)
    print("Sua compra ficou no total de {}$, com desconto de 5%".format(total))
elif opçao == 3:
    total = preço
    parcela =total / 2
    print("Sua compra ficará no valor de {:.1f}$ parcelada em 2x".format(parcela))
elif opçao == 4:
    total = preço + (preço * 3/100)
    parcela = total / 3
    print("Sua compra ficara no valor de {:.1f}$ com parcelas de:{:.1f}".format(total, parcela))
else:
    total = 0
    print("\33[31m Opção é inválida.")
