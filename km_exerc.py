speed = float(input("Qual a velocidade atual do carro?"))
if speed > 80:
    print("MULTADO,você excedeu o limite permitido que é de: 80Km/H")
    print("Tenha um bom dia e dirija com segurança!")
    multa = (speed - 80) * 7
    print("O valor da sua multa é de {:.2f} reais".format(multa))



