salario = int(input("Digite seu salario: ")) 
aumento = int(input("Digite o valor do aumento: "))

valorAumento = aumento/100
valorTotal = salario *  (1+valorAumento)


print(valorTotal)