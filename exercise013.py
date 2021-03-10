salario = float(input('Qual o salário do funcionário? R$ '))
reajuste = salario*0.15
print('O funcionário que ganhavara R$ {:.2f}, com 15% de aumento, passa a receber {:.2f}'
  .format(salario, reajuste+salario))
