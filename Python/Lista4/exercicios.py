nota = [] #da inicio a uma nova lista chamada "nota"
k = 0 #contagem do número de notas incluidas na lista 
soma = 0 #declara a soma

while k <= 3:
    nota.append(float(input('Nota')))
    soma = soma + nota[k]
    k = k +1 
print(f'A média da soma {soma} é {soma/k}')


