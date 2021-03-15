from time import sleep

def contagem(inicio, final, passo):
  print(f'Contagem de {inicio} até {final} de {passo} em {passo}:')
  sleep(1)
  if inicio < final:
    for i in range(inicio, final+passo, passo):
      print(f'{i} ', end='')

  else:
    for i in range(inicio, final-passo, -passo):
      print(f'{i} ', end='')
  print('')


contagem(1,10,1)
contagem(10,0,2)

inicio = int(input('Inicio: '))
final = int(input('Final: '))
passo = int(input('Passo: '))
contagem(inicio, final, passo)
