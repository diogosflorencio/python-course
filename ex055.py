lista_pesos = [0, 0, 0, 0, 0]
for pessos in range(0, 5):
    peso = float(input('Qual seu peso? '))
    lista_pesos[pessos] = peso
print(f' maior peso: {max(lista_pesos)} \n menor peso: {min(lista_pesos)}')