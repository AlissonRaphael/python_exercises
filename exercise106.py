def titulo(msg):
  print('-'*50)
  print(f'{msg}'.center(50))
  print('-'*50)


def biblioteca(cmd):
  titulo(f'Acessando o manual do comando {cmd}')
  help(cmd)


while True:
  titulo(f'Sistema de ajuda PyHelp')
  opcao = str(input('Insira a biblioteca ou função [F/Encerrar]: ')).strip()
  if opcao in 'Ff':
    titulo(f'Obrigado! Volte sempre.')
    break

  biblioteca(opcao)
