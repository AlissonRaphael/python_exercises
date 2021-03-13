num1 = int(input('Insira o número 1: '))
num2 = int(input('Insira o número 2: '))

opcao = 0
while opcao != 5:
  print('1 - Somar\n2 - Multiplicar\n3 - Maior\n4 - Novos números\n5 - Encerrar')
  print('-'*40)
  opcao = int(input('Insira a opção escolhida [1 ,2 ,3 ,4 ou 5]: '))

  if opcao == 1:
    print('Soma: {} + {} = {}'.format(num1, num2, num1+num2))
  elif opcao == 2:
    print('Multiplicar: {} x {} = {}'.format(num1, num2, num1*num2))
  elif opcao == 3:
    if num1 > num2:
      print('O maior número é {}'.format(num1))
    elif num1 < num2:
      print('O maior número é {}'.format(num2))
    else:
      print('Os números são iguais!')

  elif opcao == 4:
    num1 = int(input('Insira o número 1: '))
    num2 = int(input('Insira o número 2: '))
  elif opcao == 5:
    print('Fim da execução, volte sempre!')
  else: 
    print('Opção inválida!')
