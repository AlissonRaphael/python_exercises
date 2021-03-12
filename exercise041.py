from datetime import date

nascimento = int(input('Insira o ano de nascimento: '))
idade = date.today().year - nascimento

if idade <= 9:
  print('Mirim')
elif idade <= 14:
  print('Infantil')
elif idade <= 19:
  print('Junior')
elif idade <= 25:
  print('Sênior')
else:
  print('Master')
