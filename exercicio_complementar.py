velocidade =  int(input("Digite a velocidade do carro: "))
multa = (velocidade - 110)*5

if velocidade > 110 :
    print("Multado em R$", multa)
else :
    print("Velocidade Perfeita")