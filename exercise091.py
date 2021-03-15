from random import randint
from time import sleep
from operator import itemgetter

jogos = dict()
for i in range(0, 4):
  valor = randint(1,6)
  jogos[f'Jogador {i+1}'] = valor
  print(f'Jogador {i+1} tirou {valor}.')
  sleep(1)

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print('-'*30)
print(f'Ranking'.center(30))
print('-'*30)

for keys, values in enumerate(ranking):
  print(f'{keys+1}º colocado: {values[0]} com {values[1]}.')
