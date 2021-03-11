from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo: '))

print('O ângulo de {} tem seno de {:.2f}'.format(angulo, sin(radians(angulo))))
print('O ângulo de {} tem cosseno de {:.2f}'.format(angulo, cos(radians(angulo))))
print('O ângulo de {} tem tangente de {:.2f}'.format(angulo, tan(radians(angulo))))
