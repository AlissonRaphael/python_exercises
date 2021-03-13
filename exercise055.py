menor = 0
maior = 0

for i in range(1, 6):
  peso = int(input('Insira o peso da {}ª pessoa (kg): '.format(i)))

  if i == 1:
    menor = peso
    maior = peso
  elif peso < menor:
    menor = peso
  elif peso > maior:
    maior = peso

print('O menor peso lido é {}. O maior peso lido é {}.'.format(menor, maior))
