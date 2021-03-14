palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis',
  'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programar', 'Futuro')

for palavra in palavras:
  print(f'Na palavra {palavra}, temos as vogais: ', end='')
  for letra in palavra:
    print(f'{letra} ' if letra in 'AEIOUaeiou' else '', end='')
  print('')
