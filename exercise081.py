dados = []

while True:
  novo_dado = int(input('Digite um valor: '))
  
  dados.append(novo_dado)
  
  opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
  if opcao == 'N':
    break

dados.sort(reverse=True)
print(f'Você digitou {len(dados)} valor(es).')
print(f'Os valores em ordem decrescente são: {dados}.')
print(f'O valor 5 faz parte da lista' if dados.count(5) else 'O valor 5 não faz parte da lista.')
