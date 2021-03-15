dados = []

while True:
  dado = int(input('Insira um valor: '))

  if dado in dados:
    print(f'O valor {dado} já foi adicionado, tente um novo.')
  else:
    dados.append(dado)

  opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
  if opcao == 'N':
    break

dados.sort()
print(f'O valores inseridos foram {dados}.')
