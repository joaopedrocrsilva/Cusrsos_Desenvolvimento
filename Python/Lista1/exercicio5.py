valorMercadoria = int(input("Valor da Mercadoria"))
valorDesconto = int(input("valor Desconto"))

desconto = 1 - (valorDesconto/100)
valorTotal = valorMercadoria - (1 - (valorDesconto/100))

print(desconto)
print(valorTotal)