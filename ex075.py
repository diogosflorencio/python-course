primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite um valor: '))
terceiro_valor = int(input('Digite um valor: '))
quarto_valor = int(input('Digite um valor: '))
tupla = (primeiro_valor, segundo_valor, terceiro_valor, quarto_valor)
print(f'O número nove apareceu {tupla.count(9)} vezes!')
if tupla.count(3) > 0: # ou: if 3 in tupla:
    print(f'O número três foi digitado na {tupla.index(3)+1}ª posição!')
else:
    print('Não tem 3 nessa tupla!')
lista_de_pares = []
if tupla[0] % 2 == 0:
    lista_de_pares.append(tupla[0])
if tupla[1] % 2 == 0:
    lista_de_pares.append(tupla[1])
if tupla[2] % 2 == 0:
    lista_de_pares.append(tupla[2])
if tupla[3] % 2 == 0:
    lista_de_pares.append(tupla[3])
print(f'Estes foram os pares dessa dupla: {lista_de_pares}')

