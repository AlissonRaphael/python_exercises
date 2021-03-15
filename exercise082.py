dados = []
pares = []
impares = []

while True:
  novo_dado = int(input('Digite um valor: '))
  dados.append(novo_dado)
  
  if novo_dado%2 == 0:
    pares.append(novo_dado)
  else:
    impares.append(novo_dado)
  
  opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
  if opcao == 'N':
    break

print(f'A lista completa é: {dados}.')
print(f'A lista de pares é: {pares}.')
print(f'A lista de impares é: {impares}.')
