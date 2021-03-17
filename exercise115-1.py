def titulo(titulo):
  print('-'*40)
  print(f'{titulo}'.center(40))
  print('-'*40)


def menu(opcoes):
  for index, opcao in enumerate(opcoes):
    print(f'{index+1} - {opcao}')
  
  print('-'*40)


def leiaopcao(msg):
  while True:
    try:
      opcao = int(input(msg))
    except(ValueError, TypeError):
      print('Inválido! Digite uma das opções acima.')
      continue
    except(KeyboardInterrupt):
      print('O usuário preferiu não informar o número.\nEncerrando execução!.')
      return 3
    
    return opcao


titulo('Menu principal')
menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do Sistema'])
while True:
  opcao = leiaopcao('Sua opção: ')
  if opcao == 1:
    titulo('Pessoas cadastradas')
  elif opcao == 2:
    titulo('Cadastrar novas pessoas')
  elif opcao == 3:
    titulo('Sair do Sistema')
    break
  else:
    print('Inválido! Digite uma das opções acima.')

