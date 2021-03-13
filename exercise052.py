numero = int(input('Insira o último termo: '))

for termo in range(1, numero+1):
  if numero % termo == 0:
    print('\033[34m{}'.format(termo), end='')
  else:
    print('\033[m{}'.format(termo), end='')
  
  print('\033[m ', end='')
