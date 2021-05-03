a = int(input('lado a: '))
b = int(input('lado b: '))
c = int(input('lado c: '))

if a> b + c or b > a + c or c > a + b:
    print('Não Pode Ser Um Triângulo')
elif a == b == c:
    print('Equilátero')
elif a == b or b == c or a == c:
    print('Isóceles')
else:
    print('Escaleno')