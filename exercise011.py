l = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))

a = l*h
q = a/2
print('Sua parede tem dimensão {:.2f}x{:.2f} e sua área é {:.2f}.'
  .format(l, h, a))
print('Para pintar essa parede, você precisará de {:.2f}L de tinta.'
  .format(q))
