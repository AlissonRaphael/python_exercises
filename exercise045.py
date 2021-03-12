from random import randint
from time import sleep

print('Game Pedra/Papel/Tesoura\n[1] - Pedra\n[2] - Papel\n[3] - Tesoura')
jog = int(input('Escolha sua opção [1, 2 ou 3]: '))
pc = randint(1,3)
opcoes = ['Pedra', 'Papel', 'Tesoura']

print('Pedra...')
sleep(1)
print('Papel...')
sleep(1)
print('Tesoura...')

if pc == jog:
  print('Empatou! Os dois escolheram {}.'.format(opcoes[jog-1]))
elif pc == 1 and jog == 2 or pc == 2 and jog == 3 or pc == 3 and jog == 1:
  print('Ganhou! Você jogou {} e o computador jogou {}.'.format(opcoes[jog-1], opcoes[pc-1]))
elif jog == 1 and pc == 2 or jog == 2 and pc == 3 or jog == 3 and pc == 1:
  print('Perdeu! Você jogou {} e o computador jogou {}.'.format(opcoes[jog-1], opcoes[pc-1]))
