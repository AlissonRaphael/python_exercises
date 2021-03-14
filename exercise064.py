soma = 0
quantidade = 0
controle = True
while controle:
  numero = int(input('Insira um número [999/Cancelar]: '))

  if numero == 999:
    controle = False
  else:
    soma += numero
    quantidade += 1

print('Você digitou {} números e a somatório é {}.'.format(quantidade, soma))
