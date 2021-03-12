from random import randint

print('-=-'*9)
print('Acerte o número de 0 á 5')
print('-=-'*9)

num = int(input('Adivinhe o número sorteado: '))
sorteado = randint(0,5)

if num == sorteado:
  print('Acertou! Você colocou {} e foi sorteado {}.'.format(num, sorteado))
else:
  print('Errou! Você colocou {} e foi sorteado {}.'.format(num, sorteado))
