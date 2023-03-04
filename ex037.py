num = int(input('Digite um número: '))
print('''Qual conversão vc deseja fazer? 
[1] binário
[2] octal
[3] hexadecimal''')
escolha = int(input('Escolha! '))
if escolha == 1:
    print(f'{num} em binário é {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} em octal é {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} em hexadecimal é {hex(num)[2:]}')
else:
    print('escolha inválida! ')