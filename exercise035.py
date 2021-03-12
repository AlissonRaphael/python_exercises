seg1 = float(input('Tamanho do segmento I: '))
seg2 = float(input('Tamanho do segmento II: '))
seg3 = float(input('Tamanho do segmento III: '))

if seg1+seg2 > seg3 and seg1+seg3 > seg2 and seg2+seg3 > seg1:
  print('Os segmentos podem formar um triângulo.')
else:
  print('Os segmentos não podem formar um triângulo.')
