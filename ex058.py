''''#qts = int(input('qual a quantidade de paredes (máximo 2)? '))
#if qts == 1:
#  igual = input('essa parede tem todos os lados iguais? ')
#if qts == 2:
#  iguais = input('essas paredes têm todos os lados igual? ')

from random import randint
from time import sleep
n = randint(0,5)
print('--|--|--| JOGO DA ADIVINHAÇÃO |--|--|--')
#sleep(2)
print('-----------------------------------------')
print('O computador está gerando um número...')
print('')
#sleep(4)
user = int(input('Adivinhe o número! Escreva um número entre 0 e 5 e veja se vc acertou: '))
#sleep(1)
print('O computador está comparando os números...')
#while sleep(3):
#  print('.')
#sleep(2)
print(n)
if user > n:
  while user > n:
    user = int(input('tente um número menor: '))
    if user == n:
      print('Acertou')
if user < n:
  while user < n:
    user = int(input('tente novamente com um número maior: '))
    if user == n:
      print('acertou!')


#if user3 == n or user2 == n or user == n:
#  print('acertou!')'''

import random

finalizacao = '?'
while finalizacao != 'S' or finalizacao != 'N':
    numero_aleatorio = random.randint(0, 10)
    user_num = 'a'
    x = 0
    while user_num != numero_aleatorio:
        x = x + 1
        user_num = int(input('Digite um número: '))
        if user_num > numero_aleatorio:
            print('Digite um número menor!')
        elif user_num < numero_aleatorio:
            print('Digite um numero maior: ')
        else:
            break
    print(f'Você acetou! O numero era {numero_aleatorio} e vc precisou chutar {x} vezes!')
    continuar = input('Quer continuar [S/N]').upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('Não entendi. Quer continuar [S/N] ').upper()
    if continuar == 'N':
        break


