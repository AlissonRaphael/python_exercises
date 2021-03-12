distancia = float(input('Qual a distância? '))

if distancia <= 200:
  print('Preço: R$ {:.2f}'.format(distancia*0.5))
else:
  print('Preço: R$ {:.2f}'.format(distancia*0.45))
