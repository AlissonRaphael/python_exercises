numero = int(input('Insira o número para calcular o fatorial: '))
print('Calculando {}! = '.format(numero), end='')

fatorial = 1
while numero > 0:
  print('{} = '.format(numero) if numero == 1 else '{} x '.format(numero), end='')
  fatorial *= numero
  numero -= 1

print(fatorial)
