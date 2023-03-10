#programa que lê um numero entre 0 e 9999 e mostre ele separadamente. unidade, dezena, centena

numero = input('Digite um número: ')
quantidade = len(numero)
print(quantidade)
if quantidade == 4:
    print(f'unidade: {numero[3]}')
    print(f'dezena {numero[2]}')
    print(f'centena {numero[1]}')
    print(f'milhar {numero[0]}')

if quantidade == 3:
    print(f'unidade: {numero[2]}')
    print(f'dezena {numero[1]}')
    print(f'centena {numero[0]}')

if quantidade == 2:
    print(f'unidade: {numero[1]}')
    print(f'dezena {numero[0]}')

if quantidade == 1:
    print(f'unidade: {numero[0]}')
