numeros = (
  int(input('Insira o número 1: ')),
  int(input('Insira o número 2: ')),
  int(input('Insira o número 3: ')),
  int(input('Insira o número 4: ')),
)

print(f'Você digitou os valores {numeros}.')
print(f'O número 9 aparece {numeros.count(9)} veze(s).')
print(f'O número 3 aparece {numeros.index(3)+1}ª posição.')
print('Os valores pares digitados foram: ', end='')
for n in numeros:
  print(f'{n} ' if n%2 == 0 else '', end='')
