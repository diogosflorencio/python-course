lista_impar = [0,0,0,0,0,0]
soma = 0
for index in range(0, 6):
    numero = int(input('Digite um valor: '))
    is_par = numero % 2 == 0
    if is_par:
        soma += numero
    elif numero % 2 != 0:
        lista_impar[index] = numero
print(f'a soma dos numeroes pares é igual a: {soma}. \n esse numeros impares n fora somados: {lista_impar}')
