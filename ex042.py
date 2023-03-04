reta1 = float(input('Primeira reta: '))
reta2 = float(input('Segunda reta: '))
reta3 = float(input('Terceira reta: '))
lista_de_retas = reta3, reta2, reta1
maior_reta = max(lista_de_retas)
soma_das_retas_menores = (reta3+reta2+reta1) - maior_reta
print(soma_das_retas_menores)
if soma_das_retas_menores > maior_reta:
    if reta2 == reta3 and reta3 == reta1:
        print('pode ser um triangulo e ele será equilatero')
    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
        print('triangulo e é um escaleno ctz')
    else:
        print('é um triangulo e é isósceles')
else:
    print('n pode ser um triangulo')


