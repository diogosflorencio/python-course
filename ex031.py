distancia = float(input('qual será a distancia? '))
'''if distancia <= 200:
    print(f'sua viagem custará R$ {distancia*0.5}')
else:
    print(f'sua viagem custará {distancia*0.45}')'''
print(distancia*0.5 if distancia <= 200 else distancia*0.45)

