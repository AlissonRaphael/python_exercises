from random import randint

sorteado = randint(1,10)
print('---- Adivinhe o número entre 1 e 10 ----')

condicao = True
tentativas = 0
while condicao:
  palpite = int(input('Digite seu palpite: '))
  tentativas += 1

  if sorteado == palpite:
    print('Acertou! O palpite foi {} e o sorteado foi {}.'.format(palpite, sorteado))
    condicao = False
  elif sorteado < palpite:
    print('Errou! É menos, tente novamente.')
  elif sorteado > palpite:
    print('Errou! É mais, tente novamente.')
