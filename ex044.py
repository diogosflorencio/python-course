nome_da_loja = " POTTER'S "
print(f'{nome_da_loja:=^100}')
valor = float(input('Digite o valor do produto à ser pago: '))
forma_de_pagamento = str(input('Qual será a forma de pagamento? (escolha entre: cartão, dinheiro e cheque): '))
if forma_de_pagamento == 'dinheiro' or forma_de_pagamento == 'cheque':
    print(f'Você terá 10% de desconto pagando em dinheiro ou cheque, logo, o valor final do protudo será: {valor-(0.1*valor)}. Obrigado pela compra, volte sempre!')
while forma_de_pagamento == 'cartão' or forma_de_pagamento == 'cartao' or forma_de_pagamento == 'cartão de credito':
    vezes = int(input('O pagamento será parcelado em quantas vezes? '))
    if vezes == 1:
        print(f'À vista no cartão, você terá um desconto de 5%, o que deixará o valor final igual à: {valor-(valor*0.05)}. Obrigado pela sua compra!')
    elif vezes == 2:
        print(f'Parcelando em duas vezes no cartão, vc não terá juros, pagará 2x de {valor/2}. Obrigado!')
    elif vezes >= 3:
        print(f'Parcelando em {vezes} no cartão, sua compra terá um juros de 20%. o valor a ser pago é de {vezes}x de {(valor+(0.2*valor))/vezes}, no total, R$ {valor+(0.2*valor)}. Obrigado, volte sempre!')
        break
