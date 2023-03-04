'''from random import randint
from time import sleep
contvitoria = 0
while True:
    pc = randint(0, 10)
    usernumero = int(input('Digite um valor: '))
    userescolha = input('Digite I para impar e P para par: ').upper().strip()[0]
    soma = pc + usernumero
    if userescolha == 'I':
        pcescolha = 'P'
    else:
        pcescolha = 'I'
    if soma % 2 == 0:
        vitoria = 'P'
    else:
        vitoria = 'I'
    if userescolha == vitoria:
        contvitoria = contvitoria + 1
        print(f'vc ganhou! deu {vitoria}. vitoria = {contvitoria} + 1')
    else:
        print(f'vc perdeu! deu {vitoria}, mas vc ganhou {contvitoria} vezes')
        break'''

from random import randint
user_victory = 0
while True:
  numero_pc = randint(0, 10)
  numero_user = int(input('Digite um número de 0 a 10: '))
  escolha_do_user = input('IMPAR ou PAR? ').upper()
  resultado = numero_pc + numero_user
  if resultado % 2 == 0:
    resultado = 'PAR'
    print('Deu PAR!')
    if resultado == escolha_do_user:
      print('Você ganhou!')
      user_victory +=1
    else:
      print('O PC ganhou!')
      print(f'Você ganhou {user_victory} vezes!')
      break
  else:
    resultado = 'IMPAR'
    print('Deu IMPAR!')
    if resultado == escolha_do_user:
      print('Você ganhou!')
      user_victory +=1
    else:
      print('O PC ganhou!')
      print(f'Você ganhou {user_victory} vezes!')
      break
