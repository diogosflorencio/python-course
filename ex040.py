nota1 = float(input('qual sua primeira nota? '))
nota2 = float(input('qual seu segunda nota? '))
media = (nota1+nota2)/2
if media >= 7:
    print('parabéns, vc foi aprovado!')
elif media >= 5 and media <= 6.9:
    print('Vc está de recuperação!')
else:
    print('reprovado!')
