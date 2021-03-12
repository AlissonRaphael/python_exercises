from datetime import date

nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento

if idade > 18:
  print('Você tem {} anos. Deveria ter se alistado á {} anos.'.format(idade, idade-18))
elif idade < 18:
  print('Você tem {} anos. Deverá se alistar em {} anos.'.format(idade, 18-idade))
else:
  print('Voce tem 18 anos, deverá se alistar imediatamente.')
