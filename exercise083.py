expressao = str(input('Digite a expressão: ')).strip()
abre = []
fecha = []

for i in expressao:
  if i == '(':
    abre.append(i)
  elif i == ')':
    fecha.append(i)

print(f'Sua expressão está ', end='')
print('válida.' if len(abre) == len(fecha) else 'inválida.')
