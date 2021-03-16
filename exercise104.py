def leia_inteiro(msg):
  controle = True
  while controle:
    n = str(input(msg))

    if n.isnumeric():
      n = int(n)
      controle = False
    else:
      print('Erro! Digite um valor inteiro válido.')

  return int(n)


numero = leia_inteiro('Digite um número inteiro: ')
print(f'Você digitou {numero}.')
