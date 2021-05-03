minutos = int(input("Digite a quantidade de minutos"))

if minutos < 200:
    valor = 0.2

elif minutos <= 400:
    valor = 0.18

elif minutos <= 800:
    valor = 0.15

else:
    valor = 0.08


print (f'R$ {valor*minutos: .2f}')







