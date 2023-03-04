lista = []
for posicao in range(5):
    lista.append(int(input('Digite um valor: ')))
minimo = min(lista)
maximo = max(lista)

print(f'o maior valor é {maximo}, nas posições: ', end='')
for index, valores_da_lista in enumerate(lista):
    if valores_da_lista == maximo:
        print(f'{index}', end='...')

print(f'o menor valor é {minimo}, nas posições: ', end='')
for index, valores_da_lista in enumerate(lista):
    if valores_da_lista == minimo:
        print(f'{index}', end='...')