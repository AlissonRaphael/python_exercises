numeros = [[],[]]

for i in range(1, 8):
  numero = int(input(f'Insira o {i} número: '))

  if numero%2 == 0:
    numeros[0].append(numero)
  else:
    numeros[1].append(numero)

print('-'*40)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
