print('---- Loja Super Baratão ----')

acima_mil = total = 0
barato = None
nome_protudo = ''

while True:
  nome = str(input('Nome do Produto: ')).strip()
  preco = float(input('Insira o Preço: R$ '))
  
  total += preco
  
  if preco >= 1000:
    acima_mil += 1
  
  if barato == None:
    barato = preco
    nome_protudo = nome
  elif preco < barato:
    barato = preco
    nome_protudo = nome
  
  opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
  if opcao == 'N':
    break

print(f'Total da compra foi R$ {total:.2f}')
print(f'Quantidade de produtos custando mais de mil: {acima_mil}')
print(f'O produto mais barato foi {nome_protudo}, custando R$ {barato:.2f}')
