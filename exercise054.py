from datetime import date

menores = 0
maiores = 0

for i in range(1, 8):
  nascimento = int(input('Data de nascimento da {}ª pessoa: '.format(i)))

  idade = date.today().year - nascimento

  if idade < 18:
    menores += 1
  else:
    maiores += 1

print('Temos {} pessoa(s) menores e {} pessoa(s) maiores de idade.'.format(menores, maiores))
