KM = float(input("Quantos KM's você irá percorrer?"))
if KM <= 200:
    preço = KM * 0,50
else:
    preço = KM * 0,45
    print("O preço de sua passagem será de {:.2f}$ reais".format(preço))