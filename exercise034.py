salario = float(input('Digite o salário: R$ '))

if salario >= 1250:
  print('Com reajuste de 10%, o novo salário é R$ {:.2f}'.format(salario+salario*0.1))
else:
  print('Com reajuste de 15%, o novo salário é R$ {:.2f}'.format(salario+salario*0.15))
