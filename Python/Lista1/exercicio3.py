dias = int(input("Digite a quantidade de dias: "))
horas = int (input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundo = int(input("Digite a quantidade de segundos: "))

segundostotal = ((dias*24*60*60) + (horas*60*60) + (minutos*60) + segundo)

print("O valor em segundo e:")
print(segundostotal)
