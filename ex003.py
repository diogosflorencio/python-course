#expressões com variáveis

cor = '\033[1;31;40m'
coroff = '\033[m'
print(f'{cor}=== desafio 3 ==={coroff}')
print('para somar, digite as duas parcelas em sequencia... ')
n1 = float(input('qual o primeiro númeor/parcela? '))
n2 = float(input('agora a segunda parcela: '))
print(f'a soma das parcelas é igual a {cor}{n1+n2:.1f}', n1+n2, end='')
print('wow')
