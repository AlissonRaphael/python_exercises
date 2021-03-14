brasileiro = ('Flamengo','Internacional','Atlético-MG','São Paulo','Fluminense','Grêmio',
  'Palmeiras','Santos','Athletico-PR','Bragantino','Ceará SC','Corinthians','Atlético-GO',
  'Bahia','Sport Recife','Fortaleza','Vasco da Gama','Goiás','Coritiba','Botafogo')

print('---'*30)
print(f'Times brasileiros: {brasileiro}')
print('---'*30)
print(f'Classificados para Libertadores: {brasileiro[:4]}')
print('---'*30)
print(f'Classificados para Pré-libertadores: {brasileiro[4:6]}')
print('---'*30)
print(f'Classificados para Sulamericana: {brasileiro[6:12]}')
print('---'*30)
print(f'Rebaixados: {brasileiro[16:]}')
