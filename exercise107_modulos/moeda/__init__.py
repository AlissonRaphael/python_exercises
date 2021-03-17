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

