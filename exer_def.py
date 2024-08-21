def melhor(laRoche, creamy, payot):
    melhor = laRoche
    if creamy > melhor:
        melhor = creamy
        if payot > melhor:
            melhor = payot
            return melhor


def pior(laRoche, creamy, payot):
    pior = laRoche
    if payot > pior:
        pior = payot
        if creamy > pior:
            pior = creamy
            return pior


def menu() -> object: laRoche, creamy, payot
laRoche = str(input("Insira seu primeiro produto de skincare: "))
creamy = str(input("Insira seu segundo produto de skincare: "))
payot = str(input("Insira seu último produto de skincare: "))

print("A melhor marca de skincare é{}: ".format(melhor))
print("A pior marca de skincare é{}: ".format(pior))


while True:
    menu()