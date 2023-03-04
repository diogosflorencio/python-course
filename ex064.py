contador = 0
soma = 0
while True:
    user = int(input('digite qualquer valor e 999 pra parar '))
    soma = soma + user
    contador += 1
    if user == 999:
        break
print(f'digitou {contador-1} numeros, somando {soma-999}')