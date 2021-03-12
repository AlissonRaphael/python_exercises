valor = float(input('Valor da casa: R$ '))
salario = float(input('Salário: R$ '))
tempo = int(input('Quantos anos pretende pagar? '))

prestacao = valor/(tempo*12)

if salario*0.3 < prestacao:
  print('Desculpe, emprestido negado.')
else:
  print('Aprovado! O valor da prestação é R$ {:.2f}'.format(prestacao))
