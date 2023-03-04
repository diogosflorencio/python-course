valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
while True:
    menu = int(input('O que vc deseja fazer? '
                     '\n[1] somar'
                     '\n[2] multiplicar'
                     '\n[3] maior'
                     '\n[4] novos números '
                     '\n[5] sair do programa\n '))
    if menu == 1:
        soma = valor2 + valor1
        print(f'{valor1} + {valor2} = {soma}')
        print()
    elif menu == 2:
        mult = valor2 * valor1
        print(f'{valor1} x {valor2} = {mult}')
        print()
    elif menu == 3:
        if valor1 > valor2:
            print(f'{valor1} é maior!')
        else:
            print(f'{valor2} é maior!')
            print()
    elif menu == 4:
        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))
    elif menu == 5:
        break
    else:
        print('Valor não permitido!')
