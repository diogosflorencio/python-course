num = int(input('núm par ou ímpar: '))
#print('ímpar' if num[-1] in ('1', '3', '5', '7', '9') else 'par')
resultado = num % 2
if resultado == 1:
    print(f'{num} é ímpar!')
else:
    print(f'{num} é par!')