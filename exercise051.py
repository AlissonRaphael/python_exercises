print('-'*25)
print('10 Termos de uma PA'.center(25))
print('-'*25)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1)*razao

for termo in range(primeiro, decimo, razao):
  print('{}'.format(termo), end=' -> ')

print('Fim')
