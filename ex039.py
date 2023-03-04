import datetime
anoatual = datetime.date.today().year
nascimento = int(input('Em qual ano tu nascestes? '))
sexo = input('Vc é homem ou mulher? [M] MULHER, [H] HOMEM: ')
sexo = sexo.upper()
idade = anoatual-nascimento
atraso = idade-18
adiantamento = 18-idade
if idade < 18 and sexo == 'H':
    print(f'Ainda não está na hora do seu alistamento, te falta {adiantamento} anos, ou seja, vc irá se alistar em {anoatual+adiantamento}!')
elif idade > 18 and sexo == 'H':
    print(f'já passou da hora do seu alistamento. Vc está {atraso} anos atrasado, ou seja, devia ter ido em {anoatual-atraso}!')
elif idade == 18 and sexo == 'H':
    print('Está na hora certa de vc ir se alistar, corre maluco, senão o estado vai comer seu')
else:
    print('Mulher n se alista.')