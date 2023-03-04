numbersofibonacci = int(input('Quantos elementos vc quer ver da sequencia de fibonacci? '))
termo1 = 0
termo2 = 1
print(termo1)
print(termo2)
contador = 3
while contador <= numbersofibonacci:
    termo3 = termo1 + termo2
    print(termo3)
    termo1 = termo2
    termo2 = termo3
    contador = contador + 1
