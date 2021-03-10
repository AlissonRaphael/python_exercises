preco = float(input('Qual é o preço do produto? '))
desconto = preco*0.05

print('O produto que custava R$ {:.2f}, na promoção de 5% vai custar {:.2f}'
  .format(preco, preco-desconto))
