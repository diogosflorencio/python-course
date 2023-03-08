#usando biblioteca 

import math
from math import floor

numero = float(input('Digite um numero qualquer e receba ele inteiro: '))
inteirização = floor(numero)
inteirização2 = math.trunc(numero)
print(f'o a parte inteira de {numero} é {inteirização} ou {inteirização2}')