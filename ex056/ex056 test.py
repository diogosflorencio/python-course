
lista_idades = [0, 0, 0, 0]
soma_idades = 0

#repete as 3 perguntas 4 vezes
for index in range(0, 4):
    #faz as tres perguntas
    nome = input('Qual é o seu nome? ')
    idade = int(input('Qual é sua idade? '))
    sexo = input('Qual é o seu sexo? ')

    #verifica se é masculo, coloca na lista em ordem crescente e printa a maior idade

    if sexo == 'masculino':
        lista_idades[index] = idade
lista_idades.sort()
print(f'maior idade é {lista_idades[-1]}')

#soma_idades = soma_idades + idade
#media_idades = soma_idades / 4
