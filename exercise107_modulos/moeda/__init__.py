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


def porcentagem(preco, porcentagem, reduzir=False, show_cifrao=False):
  if reduzir:
    resultado = preco-preco*(porcentagem/100)
  else:
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
  print(f'{aumento}% do preço: {porcentagem(numero, aumento, show_cifrao=True)}')
  print(f'{reducao}% do preço: {porcentagem(numero, reducao, reduzir=True, show_cifrao=True)}')
  print('-'*40)