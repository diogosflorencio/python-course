#usando random

import random
aluno1 = input('nome do aluno 1: ')
aluno2 = input('nome do aluno 2: ')
aluno3 = input('nome do aluno 3: ')
aluno4 = input('nome do aluno 4: ')
lista = (aluno4, aluno3, aluno2, aluno1)
escolha = random.choice(lista)
print(f'quem vai apagar é o {escolha}')
