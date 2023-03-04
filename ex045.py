import random
from time import sleep
print('-='*3, 'THE ROCK, PAPER AND CUTTER!', '-='*3)
sleep(1)
print('iniciando o jogo...')
sleep(1)
print()
jogo = 'on'
while jogo == 'on':
    user = input('PEDRA, PAPEL OU TESOURA? ')
    user = user.upper()
    aleatorio = ['PEDRA', 'PAPEL', 'TESOURA']
    aleatorio = random.choice(aleatorio)
    print('COMPUTADOR ESCOLHENDO...')
    sleep(2)
    if aleatorio == user:
        print(f'VC: {user}')
        sleep(1)
        print(f'COMPUTADOR: {aleatorio}')
        sleep(1)
        print('EMPATOU!!!')
        sleep(1)
        print('EMPATOU!!!')
        sleep(1)
        continuar = input('CONTINUAR? [SIM] | [NÃO] ')
        continuar = continuar.upper()
        if continuar == 'NAO' or continuar == 'NÃO' or continuar == 'N':
            break
        else:
            continue
    elif aleatorio == 'PEDRA' and user == 'TESOURA' or aleatorio == 'TESOURA' and user == 'PAPEL' or aleatorio == 'PAPEL' and user == 'PEDRA':
        print(f'VC: {user}')
        sleep(1)
        print(f'COMPUTADOR: {aleatorio}')
        sleep(1)
        print('O COMPUTADOR GANHOU!!!')
        sleep(1)
        print('O COMPUTADOR GANHOU!!!')
        sleep(1)
        continuar = input('CONTINUAR? [SIM] | [NÃO] ')
        continuar = continuar.upper()
        if continuar == 'NAO' or continuar == 'NÃO' or continuar == 'N':
            break
        else:
            continue
    elif aleatorio == 'TESOURA' and user == 'PEDRA' or aleatorio == 'PEDRA' and user == 'PAPEL' or aleatorio == 'PAPEL' and user == 'TESOURA':
        sleep(1)
        print(f'VC: {user}')
        sleep(1)
        print(f'COMPUTADOR: {aleatorio}')
        sleep(1)
        print('VC GANHOU!!!')
        sleep(1)
        print('VC GANHOU!!!')
        sleep(1)
        continuar = input('CONTINUAR? [SIM] | [NÃO] ')
        continuar = continuar.upper()
        if continuar == 'NAO' or continuar == 'NÃO' or continuar == 'N':
            break
        else:
            continue