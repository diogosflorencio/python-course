idade = int(input('qual sua idade? '))
idades = 10, 11, 12, 13, 14
if idade <= 9:
    print('vc está na categoria mirim')
elif idade in idades:
    print('vc está na categoria infantil')
elif idade > 14 and idade <= 19:
    print('vc é junior')
elif idade == 20:
    print('vc é senior')
else:
    print('vc é master')