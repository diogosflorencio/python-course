#programa que ler o preço de algo e mostra seu valor com 5% de desconto

desconto = int(input('quanto de desconto? '))
n1 = float(input(f'para saber o valor de um produto com {desconto}% digite o valor do produto: '))
print(f'vc pagará {n1 - ((desconto/100)*n1)} reais')