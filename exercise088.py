from random import randint
from time import sleep

print('-'*50)
print('Jogos na Mega Sena'.center(50))
print('-'*50)

jogo = list()
jogos = int(input('Quantidade de jogos você quer: '))
for i in range(0, jogos):

  contador = 0
  while True:
    numero = randint(1,60)

    if numero not in jogo:
      jogo.append(numero)
      contador += 1
    
    if contador == 6:
      break

  jogo.sort()
  sleep(1)
  print(f'Jogo {i+1}: {jogo}')
  jogo.clear()
