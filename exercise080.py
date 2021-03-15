dados = []

for i in range(0,4):
  novo_dado = int(input('Digite um valor: '))

  if i == 0:
    dados.append(novo_dado)
    print(f'Inserido na primeira posição.')
  elif novo_dado < dados[0]:
    dados.insert(0, novo_dado)
    print(f'Inserido na primeira posição.')
  elif novo_dado > dados[-1]:
    dados.insert(len(dados), novo_dado)
    print(f'Inserido na ultima posição.')
  else:
    for index, dado in enumerate(dados):
      if novo_dado <= dado:
        dados.insert(index, novo_dado)
        print(f'Inserido na posição: {index}')
        break
  
  print(dados)
