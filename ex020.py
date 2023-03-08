#usando random e shuffle from math

import random
import math
aluno1 = str(input('nome do aluno 1: '))
aluno2 = str(input('nome do aluno 2: '))
aluno3 = str(input('nome do aluno 3: '))
aluno4 = str(input('nome do aluno 4: '))
lista = [aluno4, aluno3, aluno2, aluno1]
random.shuffle(lista)
print(f'a ordem será {lista}')
