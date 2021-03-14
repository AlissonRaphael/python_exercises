termo = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))

controle = True
ultimo = 10
while controle:

  contador = 1
  while contador <= ultimo:
    print('{}'.format(termo) if contador == ultimo else '{} -> '.format(termo), end='')
    contador += 1
    termo += razao

  ultimo = int(input('\nQuantos termos quer mostrar a mais? '))

  if ultimo == 0:
    controle = False
