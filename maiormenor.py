def maior(x, y, z):
    max = x
    if y > max:
        max = y
        if z > max:
            max = z
    return max


def menor(x, y, z):
    minimo = x
    if y < minimo:
        minimo = y
        if z < minimo:
            minimo = z
    return minimo


def menu():
    x = int(input("Primeiro número: "))
    y = int(input("Segundo número: "))
    z = int(input("Terceiro número: "))

    print("Maior ", (maior(x, y, z)))
    print("Menor ", (menor(x, y, z)))
while True:
    menu()

