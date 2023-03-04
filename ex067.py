numero = 0
cont = 1
while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break

    while cont < 10:
        print(f'{numero} x {cont} = {numero*cont}')
        cont += 1
    cont = 0

'''#aqui o programa importará o time para atribuir alguns segundos em algumas partes, apenas para ficar legal
from time import sleep
#aqui a variavel recebera um index = a 0 para que depois seja adicionado mais um e fome o index inteiro da calculadora 
index_da_calc = 0
#aqui o programa se inicia com uma reptição
while True: 
  #aqui o programa pega o valor do user, que servirar para criar a tabuada com base nele e parar a aplicação caso seja negativo ou seja menor que zero
  valor = int(input('Digite um valor para obter sua tabuada e digite qualquer valor negativo para parar a aplicação: '))
  if valor < 0: 
    print('programa finalizando...')
    print('3')
    sleep(1)
    print('2')
    sleep(1)
    print('1')
    sleep(0.5)
    print('bye')
    break
  else:
    while index_da_calc <= 9:
    #aqui o index soma mais 1 para a finalidade que foi criado
      index_da_calc += 1
      print(f'{valor} x {index_da_calc} = {valor*index_da_calc}')
    index_da_calc = 0'''
