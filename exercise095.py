jogadores = list()
jogador = dict()
gols_partidas = list()

while True:
  jogador['nome'] = str(input('Nome do jogador: '))
  total = 0
  partidas = int(input('Insira a quantidade de partidas: '))
  for i in range(0, partidas):
    gols = int(input(f'Quantos gols na {i+1}ª partida: '))
    gols_partidas.append(gols)
    total += gols

  jogador['gols'] = gols_partidas[:]
  jogador['total'] = total

  jogadores.append(jogador.copy())

  gols_partidas.clear()
  jogador.clear()

  opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
  if opcao == 'N':
    break

print('-'*50)
print(f'{"ID":<3}{"Nome":<20}{"Gol(s)":<22}{"Total":<5}')
print('-'*50)
for index, jogador in enumerate(jogadores):
  print(f'{index:^3}{jogador["nome"]:<20}',f'{jogador["gols"]}'.ljust(20),f'{jogador["total"]:^5}')
print('-'*50)

while True:
  acao = int(input('O que deseja fazer?\n[99] - Encerra execução.\n[id] - ID do jogador para consultar mais informações.\nDigite a opção: '))
  if acao == 99:
    break
  else:
    print('-'*50)
    for index, jogador in enumerate(jogadores):
      if acao == index:
        print(f'{jogador["nome"]} jogou 5 partidas e marcou: ')
        for k, j in enumerate(jogador['gols']):
          print(f'- Na {k+1}ª partida: {j} gol(s).')
        print(f'- Total: {jogador["total"]} gol(s).')

  print('-'*50)
