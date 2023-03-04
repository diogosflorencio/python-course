#programa que lê o nome de uma cidade, e informa se o nome da cidade começa ou não com a palavra SANTO
cidade = input('Digite o nome da sua cidade: ').strip()
cidade = cidade.lower()
cidade = cidade.split()
cidade = cidade[0]
cidade = cidade.find('santo')
if cidade == 0:
        print('sim, tem santo')

else:
        print('o nome da sua cidade NÃO COMEÇA com a palavra SANTO')