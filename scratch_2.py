first = int(input('Primeiro número:'))
reason = int(input("Razão: "))
decimo = first +(10 - 1)* reason
for c in range(first,decimo + reason, reason ):
    print("{}".format(c), end ="->")
print("Acabou")