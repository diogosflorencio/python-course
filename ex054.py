maiores_de_idade = 0
menores_de_idade = 0
for idades in range(0,7):
    idade = int(input('Qual sua idade? '))
    if idade >= 21:
        maiores_de_idade += 1
    else:
        menores_de_idade += 1
print(f'há {maiores_de_idade} maiores e {menores_de_idade} menores de idade.')