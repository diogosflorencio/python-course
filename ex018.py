#cos, sin, tan, radians

from math import cos, sin, tan, radians
angulo = float(input('Digite um angulo para saber seu seno e consseno: '))
print(f'seu cosseno é {cos(radians(angulo)):.2f} e seu seno é {sin(radians(angulo)):.2f} e a tangente é {tan(radians(angulo)):.2f}')
