materiais = ('Lápis', 1.17, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print(' -'*20,'''
            LISTAGEM DE PROÇOS
''','- '*20,)
#f'''
#{materiais[0]}...........................R$     {materiais[1]:.2f}
#{materiais[2]}........................R$     {materiais[3]:.2f}
#{materiais[4]}.........................R$    {materiais[5]:.2f}
#{materiais[6]}..........................R$    {materiais[7]:.2f}
#{materiais[8]}....................R$     {materiais[9]:.2f}
#{materiais[10]}........................R$     {materiais[11]:.2f}
#{materiais[12]}.........................R$   {materiais[13]:.2f}
#{materiais[14]}.........................R$    {materiais[15]:.2f}
#{materiais[16]}...........................R$    {materiais[17]:.2f}
#''',
#'- '*20)

for posicao in range(0, len(materiais)):
    if posicao % 2 == 0:
        print(f'{materiais[posicao]:.<30}',end='')
    else:
        print(f'R${materiais[posicao]:>7.2f}')