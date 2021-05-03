quantidadeCigarros = int(input("Quantidade de cigarros consumidos por dia:  "))
anosFumando = int(input("Quantidade de anos que é fumante:  "))

quantidadeCigarros = (quantidadeCigarros * 365) * anosFumando
quantidadePerdida = ((quantidadeCigarros * 10)/60)/24

print('Quantidade de dias perdidos: ', quantidadePerdida)
