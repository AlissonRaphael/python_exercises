total = quantidade = maior = menor = 0
controle = True
while controle:
  numero = int(input('Insira um número: '))

  total += numero
  quantidade += 1

  if quantidade == 1:
    maior = numero
    menor = numero
  elif numero > maior:
    maior = numero
  elif numero < menor:
    menor = numero

  opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()
  if opcao == 'N':
    controle = False

print('Você digitou {} números e a média é {}.'.format(quantidade, total/quantidade))
print('O maior valor é {} e o menor valor é {}.'.format(maior, menor))
