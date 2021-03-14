while True:
  numero = int(input('Deseja ver a tabuada de qual número? '))

  if numero < 0:
    break

  for i in range(1,10):
    print(f'{numero} x {i} = {numero*i}')
