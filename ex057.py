sexo = 'neutro'
while True:
    sexo = input('Qual o seu sexo? [M/F] ').strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Escreva apenas "M", sem aspas para  "Mulher" e/ou "F", sem aspas para "Homem"')
    else:
        print('OK!')
        break
