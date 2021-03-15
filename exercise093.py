jogador = dict()
gols_partidas = list()
total = 0

jogador['nome'] = str(input('Nome do jogador: '))
for i in range(0, 5):
  gols = int(input(f'Quantos gols na {i+1}ª partida: '))
  gols_partidas.append(gols)
  total += gols

jogador['gols'] = gols_partidas
jogador['total'] = total

print(jogador)
print('-'*40)
print(f'- Nome: {jogador["nome"]}.')
print(f'- Quantidade de gols: {jogador["gols"]}.')
print(f'- Total de gols: {jogador["total"]}.')
print('-'*40)
print(f'O jogador {jogador["nome"]} jogou 5 partidas e marcou: ')
for k, j in enumerate(jogador['gols']):
  print(f'Na {k+1}ª partida: {j} gol(s).')
print(f'- Total: {jogador["total"]} gol(s).')
