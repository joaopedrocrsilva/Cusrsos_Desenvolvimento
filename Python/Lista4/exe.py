mes = ''' janeiro fevereiro março abril maio junho julho agosto setembro outubro
novembro dezembro'''.split()

d,m,a = input('dd/mm/aaa: ').split('/')
print(f'{d} de {mes[int(m)-1]} de {a}')
