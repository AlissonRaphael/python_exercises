n = int(input('---- Sequência Fibonacci ----\nInsira a quantidade de termos: '))

t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')

contador = 3
while contador <= n+1:
  t3 = t1 + t2
  print(' -> {}'.format(t3) if contador != n+1 else ' -> Fim', end='')
  t1 = t2
  t2 = t3
  contador += 1
