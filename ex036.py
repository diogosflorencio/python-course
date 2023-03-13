#emprestimo bancario

#n sei o que foi isso. 

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
        