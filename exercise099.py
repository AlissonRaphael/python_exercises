def analise(*valores):
  maior = 0
  for value in valores:
    if value == 0:
      maior == value
    elif value > maior:
      maior = value
  
  print('-'*30)
  print(f'Foram analisados {len(valores)} valores.')
  print(f'O maior valor é: {maior}.')


analise(4,3,4,5,2,0)
analise(1,7,9,20)
analise(2,8)
analise(5)
