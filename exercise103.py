def futdados(nome='Desconhecido', gols=0):
  if str(gols).isnumeric():
    gols = 0

  return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


nome = str(input('Nome do jogador: '))
gols = str(input('Quantidade de gols: '))
print(futdados(nome, gols))
