#fazer programa que le quantas vezes aparece a letra A, em que posição ela aparece na primeira vez e na ultima
frase = input('esscreva uma frase: ').strip().upper()
frase1 = frase.count('A')
print(f'a frase tem {frase1} As')
primeira = frase.find('A')+1
segunda = frase.rfind('A')+1
print(f'na primeira vez o A aparece na posição {primeira}')
print(f'na segunda vez o A aparece na posição {segunda}')