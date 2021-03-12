nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

if media >= 7:
  print('Aprovado! Com média {:.2f}'.format(media))
elif media >= 5 and media < 7:
  print('Recuperação! Com média {:.2f}'.format(media))
else:
  print('Reprovado! Com média {:.2f}'.format(media))
