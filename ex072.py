'''pessoa = int(input('digite um numero: '))
while pessoa > 20 or pessoa < 0:
    pessoa = int(input('digite um numero: '))
numeros = ('00zero', '01um', '02dois', '03três', '04quatro', '05cinco', '06seis', '07sete', '08oito', '09nove', '10dez', '11onze', '12doze', '13treze', '14quatorze', '15quinze', '16dezesseis', '17dezessete', '18dezoito', '19dezenove', '20vinte')
print(f'Vc digitou o número {numeros[pessoa][2:]}')'''

numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', '1dezoito', 'dezenove', 'vinte')
while True:
    pessoa = int(input('digite um numero: '))   
    if pessoa > 20 or pessoa < 0:
        pessoa = int(input('digite um numero: '))
    print(f'Vc digitou o número {numeros_extenso[pessoa]}')
    continuar = input('Quer continuar? ')
    if continuar == "N":
        break



