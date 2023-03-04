peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura*altura)
print(f'seu imc é {imc:.1f}')
if imc < 18.5:
    print('abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print('peso ideal!')
elif imc >= 25 and imc <= 30:
    print('sobrepeso!')
elif imc >= 30 and imc <=40:
    print('obesidade!')
else:
    print('obesidade mórbida!')
