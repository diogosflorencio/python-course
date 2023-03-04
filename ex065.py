contador = 0
soma = 0
listadenumeros = list()
while True:

    numeros = int(input('digite numeros aleatorias para saber o maior, menor e a media entre todos: '))
    lista = listadenumeros.append(numeros)
    listadenumeros.sort()
    contador = contador + 1
    soma = soma + numeros
    media = int(soma/contador)

    parar = input('parar? S ou N ').upper()
    if parar == 'S':
        print(media, listadenumeros[0], listadenumeros[-1])
        break

