valor = float(input('Valor pro hora: '))
horas = int(input('Horas Trabalhadas: '))
bruto = valor * horas
ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
liquido = bruto - ir - inss - sind

print (f'+Salario Bruto: \t\t {bruto: .2f}')
print (f'-IR: \t\t {ir: .2f}')
print (f'-INSS: \t\t {inss: .2f}')
print (f'-Sindicato: \t\t {sind: .2f}')
print (f'=Salario Liquido: \t\t {liquido: .2f}')