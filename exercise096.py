def area(l, c):
  return l*c

print('Controle de terrenos'.center(40))
print('-'*40)

largura = float(input('Largura [m²]: '))
comprimento = float(input('Comprimento [m²]: '))
print(f'A área de um terreno é {area(largura, comprimento)} m².')
