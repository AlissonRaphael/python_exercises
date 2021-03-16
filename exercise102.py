def fatorial(numero, show=False):
  """
    Calcula o fatorial de um numero.
    :param numero: O numero pelo qual o fatorial vai ser calculado [Obrigatorio].
    :param show: Mostra o calculo do fatorial [Opcional], Padrao: "False".
    :return: Retorna o resultado do fatorial (numero inteiro).
  """
  fatorial = 1
  for i in range(numero, 0, -1):
    fatorial *= i
    if show:
      print(f'{i} x ' if i != 1 else f'{i} = ', end='')
  
  return fatorial


print(fatorial(5, show=True))
help(fatorial)
