number = int(input('Numero: '))
cont = 0

for c in range(1, number+1):
    if number % c == 0:
        cont += 1
if cont <= 2 and cont != 1:
    print('é primo')
else:
    print('n é primo')
print(c)