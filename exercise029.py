velocidade = float(input('Digite a velocidade: '))

if velocidade >= 80:
  multa = velocidade * 7
  print('Multado por excesso de velocidade!\nValor da Multa: R$ {:.2f}.'.format(multa))
else:
  print('Tenha um bom dia e dirija com segurança.')
