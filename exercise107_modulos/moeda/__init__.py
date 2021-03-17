def dobro(preco, show_cifrao):
  resultado = preco*2
  if show_cifrao:
    return cifrao(resultado)
  else:
    return resultado


def metade(preco, show_cifrao):
  resultado = preco/2
  if show_cifrao:
    return cifrao(resultado)
  else:
    return resultado


def porcentagem(preco, porcentagem, show_cifrao):
  resultado = preco+preco*(porcentagem/100)
  if show_cifrao:
    return cifrao(resultado)
  else:
    return resultado


def cifrao(numero):
  return f'R$ {numero:.2f}'


def resumo(numero, aumento, reducao):
  print('-'*40)
  print('Resumo do valor'.center(40))
  print('-'*40)

  print(f'Preço analisado: {cifrao(numero)}')
  print(f'Dobro do preço: {dobro(numero, True)}')
  print(f'{aumento}% do preço: {porcentagem(numero,aumento, True)}')
  print(f'{reducao}% do preço: {porcentagem(numero,aumento, True)}')