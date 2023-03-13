#pode ser um triângulo?

reta1 = float(input('primeira reta: '))
reta2 = float(input('segunda reta: '))
reta3 = float(input('terceira reta: '))
cor = '\033[1;31;40m'
coroff = '\033[m'
lista = [reta1, reta2, reta3]
soma = reta1+reta2+reta3
maiorlado = max(lista)
subtrai = soma-maiorlado
if subtrai > maiorlado:
    print(f'{cor}pode ser um triangulo{coroff}')
else:
    print('n pode')
