n1 = int(input('número 1: '))
n2 = int(input('número 2: '))
n3 = int(input('número 3: '))
if n1 < n2 and n1 < n3:
    print(f'o menor é: {n1}')
if n2 < n1 and n2 < n3:
    print(f'o menor é: {n2}')
if n3 < n2 and n3 < n1:
    print(f'o menor é: {n3}')
if n1 > n2 and n1 > n3:
    print(f'o maior é: {n1}')
if n2 > n1 and n2 > n3:
    print(f'o maior é: {n2}')
if n3 > n1 and n3 > n2:
    print(f'o maior é: {n3}')
print()

#ou
lista = [n1, n2, n3]
print(f'o menor é: {min(lista)} e o maior é {max(lista)}')
