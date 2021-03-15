valores = []

for i in range(0,4):
  num = int(input(f'Insira o número da posição {i}: '))

  valores.append(num)

print(f'Os valores que você digitou são: {valores}.')
print(f'O maior valor digitado foi {max(valores)}, em: ', end='')
for k in range(0, len(valores)):
  if valores[k] == max(valores):
    print(f'{k}, ', end='')

print(f'\nO menor valor digitado foi {min(valores)}, em: ', end='')
for j in range(0, len(valores)):
  if valores[j] == min(valores):
    print(f'{j}, ', end='')
