#jogo da adivinhação 

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
#  print('acertou!')

