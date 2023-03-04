n = int(input('Digite um número para saber sua tabuada: '))
a = 0
for index in range(1, 11):
    a += 1
    print(f'{n} X {a} = {n*a}')

