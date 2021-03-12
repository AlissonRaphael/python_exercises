soma = 0

for i in range(0,6):
  numero = int(input('Insira o {} número: '.format(i+1)))

  if numero%2 == 0:
    soma += numero

print(soma)
