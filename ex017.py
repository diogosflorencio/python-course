import math
from math import sqrt
catetoO = float(input('digite o valor do cateto oposto: '))
catetoA = float(input('digite o valor do cateto adjacente: '))
cal1 = catetoO*catetoO
cal2 = catetoA*catetoA
cal3 = cal1 + cal2
cal4 = sqrt(cal3)
hi = math.hypot(catetoO, catetoA)
print(f'hipotenusa {cal4} ou {hi:.2f}')