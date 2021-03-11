from math import sqrt, floor

co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))

hi = sqrt(co**2+ca**2)

print('A hiotenusa vai medir {:.2f}.'.format(hi))
