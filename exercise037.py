print('Opções de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal')
opcao = int(input('Qual base deseja converter? [1, 2 ou 3] '))
numero = int(input('Insira o número: '))

if opcao == 1:
  print('O binário de {} é {}.'.format(numero, bin(numero)))
elif opcao == 2:
  print('O octal de {} é {}.'.format(numero, oct(numero)))
elif opcao == 3:
  print('O octal de {} é {}.'.format(numero, hex(numero)))
else:
  print('Opção inválida!')
