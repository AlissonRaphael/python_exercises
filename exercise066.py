soma = quantidade = 0
while True:
  numero = int(input('Insira um número [999/Parar]: '))

  if numero == 999:
    break

  soma += numero
  quantidade += 1

print('Você digitou {} números e a soma é {}.'.format(quantidade, soma))
