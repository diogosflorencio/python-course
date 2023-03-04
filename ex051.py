primeiro_termo_da_PA = int(input('digite o primeiro termo: '))
razao_da_PA = int(input('Digite qual será a razão: '))
decimo_termo = primeiro_termo_da_PA + 10 * razao_da_PA
for index in range(primeiro_termo_da_PA, decimo_termo, razao_da_PA):
    print(index, end=' ')
