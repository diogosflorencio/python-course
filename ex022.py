
'''

frase = 'diogo da silva florencio'

#fatiamento

print(frase[10])
print(frase[0:6])
print(frase[0:6:2])
print(frase[:6])
print(frase[0:])
print(frase[0::2])

#analise

print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,23))
print(frase.find('sil'))
print(frase.find('tiago'))
print('diogo' in frase)

#transformação

print(frase.replace('diogo', 'tiago').upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase2 = '    diougu da              silva florencio    '

print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

#divisão

frase3 = frase2.split()

print(frase2.split())

#junção

print(' '.join(frase3))  '''

#programa que le o nome completo de uma pessoa

#o nome da pessoa com dodas as letras maiúsculas

nome = input(str('Digite seu nome completo: '))
print(nome.upper())

#o nome com todas as letras minuscula

print(nome.lower())

#Quantoas letras tem o nome ao todo, sem considerar os espaços

nome = nome.split()
nome = ''.join(nome)
print(len(nome))

#quantas letras tem o primeiro nome dessa pessoa

nome2 = input("Digite o seu nome completo: ") #peguei o nome
nome2 = nome2.split() #separei o nome
print(len(nome2[0]))