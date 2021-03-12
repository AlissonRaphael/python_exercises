valor = float(input('Digite o valor do produto: R$ '))

print('Opções de pagamento:\n1 - À vista\n2 - À vista no cartão\n3 - em até 2x no cartão\n4 - 3x ou mais no cartão.')
opcao = int(input('Escolha a opção de pagamento [1, 2, 3 ou 4]: '))

if opcao == 1:
  print('Sua compra de R$ {:.2f} vai custar R$ {:.2f}.'.format(valor, valor-valor*0.1))
elif opcao == 2:
  print('Sua compra de R$ {:.2f} vai custar R${:.2f}.'.format(valor, valor-valor*0.05))
elif opcao == 3 or opcao == 4:
  parcelas = int(input('Quantas parcelas deseja pagar: '))
  if parcelas <= 2:
    print('Sua compra vai custar R$ {:.2f}. 2 vezes de R$ {:.2f}.'.format(valor, valor/2))
  else:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f}.'.format(valor, valor+valor*0.2))
    print('Você irá pagar {} vezes de R$ {:.2f}.'.format(parcelas, (valor+valor*0.2)/parcelas))
else:
  print('Opção inválida.')
