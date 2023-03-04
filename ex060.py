numero = int(input('Digite um número para saber seu fatorial: '))
cont = 1
fatorial = 1
while cont <= numero:
    fatorial = fatorial * cont
    cont = cont + 1
    print(fatorial)
print(fatorial)

numero = int(input('Digite um número para saber seu fatorial: '))
fatorial = 1
for index in range(1, numero+1):
    fatorial = fatorial * index
print(fatorial, index)

