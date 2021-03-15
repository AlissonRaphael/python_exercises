pessoas = list()
dados = list()
pesados = list()
leve = list()
menor = maior = 0

while True:
  nome = str(input('Insira o nome: '))
  peso = float(input('Insira o peso (kg): '))

  if len(pessoas) == 0:
    menor = peso
    maior = peso
  elif peso < menor:
    menor = peso
  elif peso > maior:
    maior = peso

  dados.append(nome)
  dados.append(peso)
  pessoas.append(dados[:])
  dados.clear()

  opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
  if opcao == 'N':
    break

print(f'Você cadastrou um total de {len(pessoas)} pessoa(s).')
print(f'O maior peso foi {maior} kg, de ', end='')
for pessoa in pessoas:
  print(f'{pessoa[0]} ' if pessoa[1] == maior else '', end='')
print(f'\nO menor peso foi {menor} kg, de ', end='')
for pessoa in pessoas:
  print(f'{pessoa[0]} ' if pessoa[1] == menor else '', end='')
