#criar um programa que leia o nome de uma pessoa e mostre se há ou n SILVA no nome
nome = str(input('digite seu nome para saber se vc é pobre: '))
nome = nome.upper()
#nome = nome.find('SILVA')
#if nome == -1:
#    print('comemore, mesmo que vc seja pobre por enquanto,seu futuro será maravilho. seu nome tem peso KASJDKJSD')
#else:
#        print('sim, pobre, vc tem silva no seu nome. F =(')


# ou faz assim:

if 'SILVA' in nome:
    print('tem')
else:
    print('no')
