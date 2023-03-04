for index in range(1):
    frase = input('Digite uma frase e saiba se é um palindromo: ')
    frase = frase.upper()
    frase = frase.split()
    frase = ''.join(frase)
    frase_inversa = frase[::-1]
    if frase == frase_inversa:
        print('é um polindromo!')
    else:
        print('n é um pol...')
