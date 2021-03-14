termo = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))

contador = 1
while contador <= 10:
  print('{}'.format(termo) if contador == 10 else '{} -> '.format(termo), end='')
  contador += 1
  termo += razao
