#fazer um programa que calcula a area de uma parede e mostrar qual a quantidade de tinta em litros é necessaria para pinta-lá, sabendo que cada litro de tinta pinta 2m²

print('para saber quantos litros de tinta são necessarios para pintar qualquer parece, primeiro digite o comprimento e a largura da mesma.')
n1 = float(input('digite o comprimento da parede: '))
n2 = float(input('digite a largura da parede: '))
print(f'para pintar a parar com {n1*n2} metros quadrados de area, vc precisarar de {(n1*n2)/2} litros.')
