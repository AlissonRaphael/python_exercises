def leiaInteiro(msg):
  while True:
    try:
      numero = int(input(msg))
    except(ValueError,TypeError):
      print('Inválido! Digite um número inteiro.')
      continue
    except(KeyboardInterrupt):
      print('O usuário preferiu não informar o número.')
      return 0
    else:
      return numero


def leiaReal(msg):
  while True:
    try:
      numero = float(input(msg))
    except(ValueError, TypeError):
      print('Inválido! Digite um número inteiro.')
      continue
    except(KeyboardInterrupt):
      print('O usuário preferiu não informar o número.')
      return 0
    else:
      return numero


n1 = leiaInteiro('Digite um número inteiro: ')
n2 = leiaReal('Digite um número real: ')
print(f'O número inteiro digitado foi {n1} e o número real foi {n2}')
