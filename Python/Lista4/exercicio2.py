from random import sample 
vetor = sample(range(100), 20)
pares = []
impares = []
for x in vetor:
    if x%2 == 0:
        pares.append(x)
    else:
        impares.append(x)
    
print('Vetor', vetor)
print('Pares', pares)
print('Impares', impares)
