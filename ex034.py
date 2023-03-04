salario = float(input('qual seu salario? '))
if salario > 1250:
    print(f'seu salario aumentou 10%, agora é: {((10/100)*salario)+salario}')
else:
    print(f'seu salario aumetou 15%, agora é: {(0.15*salario)+salario}')
