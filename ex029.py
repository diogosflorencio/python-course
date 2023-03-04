velo = float(input('Qual a velocidade do carro? '))
if velo > 80:
    veloamais = velo-80
    print(f'Vc pagará {7*veloamais:.2f}, por ter ultrapassado {veloamais} acima do limite')
print('n corre!')