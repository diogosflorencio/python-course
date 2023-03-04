mulheres_menores = 0
soma_idades = 0
lista_idades = [0, 0, 0, 0]
for index in range(0, 4):
    nome = str(input('Qual é o seu nome? '))
    idade = int(input('Qual é sua idade? '))
    sexo = str(input('Qual é o seu sexo? '))
    soma_idades += idade
    if sexo == 'f' and idade < 20:
        mulheres_menores = +1
    if sexo == 'm':
        lista_idades[index] = idade
        idade_maior = max(lista_idades)
        if lista_idades[index] == idade_maior:
            nome_maior = nome
media_idades = soma_idades/4
print(f'''A média das idades é: {media_idades}
O homem com maior idade é o: {nome_maior}
A quantidade de mulheres menores de 20 anos é: {mulheres_menores}
''')
