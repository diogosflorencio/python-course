'''import math
cor = '\033[1;31;40m'
coroff = '\033[m'
print(f'{cor}Olá, Mundo!!!{coroff}')

nome = str(input('Digite o nome da marca do seu carro: '))
if nome == 'gol':
    print(f'seu carrol gol é bem popular!')
elif nome in 'porche mustangue ferrari lamborguini':
    print('caralho, o cara é rico vey slc!')
elif nome == 'fusca':
    print('kkkkkkkkkk, mas de boas, adoraria ter um tbm')
else:
    print('c n tem carro?! eu tbm n, mas jaja nós teremos garai!')'''

print('Calculadora de emprestimo bancario!')
valorcasa = float(input('Qual o valor da casa que vc quer comprar? '))
salario = float(input('Qual o seu sálario? '))
anos = int(input('Em quantos anos vc irá pagar? '))
trintaporcem = (30/100) * salario
quantidademeses = anos*12
valorcasamensal = valorcasa/quantidademeses
if valorcasamensal > trintaporcem:
    print(f'Infelizmente o valor das parcelas da casa ({valorcasamensal}) excede 30% do salário ({trintaporcem}) ')
elif valorcasamensal <= trintaporcem:
    print(f'seu emprestimo está garantido, vc pagará {valorcasamensal} durante {quantidademeses} e isso consumirá {(valorcasamensal/100)*salario}')