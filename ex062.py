primeiro_razao = input('digite o primeiro termo e a razão separado por um espaço. assim: [PRIMEIRO RAZÃO] ').split()

primeiro = int(primeiro_razao[0])

razao = int(primeiro_razao[1])

contador = 0

pa = primeiro - razao

limite = 10

while contador < limite:
    contador = contador + 1
    pa = pa + razao
    print(pa)
    if contador == limite:
        mostrarmais = int(input('quer mostrar mais termos, se sim quantos? '))
        if mostrarmais > 0:
            limite = limite + mostrarmais
        else:
            break

