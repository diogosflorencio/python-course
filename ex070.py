from time import sleep
lista_produtos = []
lista_valores = []
valortotal = 0
maisdemil = 0
while True:
  produto = input('Digite o nome do produto: ')
  sleep(0.3)
  valor = float(input('Digite o preço do produto: '))
  lista_produtos.append(produto)
  lista_valores.append(valor)
  sleep(0.7)
  print('Produtos cadastrados!')
  sleep(1)
  print()
  if valor > 1000:
    maisdemil +=1
  valortotal = valortotal + valor
  maisbarato = min(lista_valores)
  index_do_mais_barato = lista_valores.index(maisbarato)
  item_mais_barato = lista_produtos[index_do_mais_barato]
  continuar = input('Cadastrar mais? ').upper()[0].strip()
  print()
  if continuar == 'N':
    break
sleep(.7)
print('calculando...')
sleep(4)
print(f'O gasto total foi de {valortotal}')
sleep(2)
print(F'Teve {maisdemil} custando mais de mil reais')
sleep(2)
print(f'o item mais barato foi {item_mais_barato}, custando {maisbarato} reais!')