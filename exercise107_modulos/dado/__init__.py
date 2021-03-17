def leia_moeda(msg):
  while True:
    moeda = str(input(msg))
    if moeda.isnumeric():
      break
    else:
      print(f'"{moeda}" é inválido! Insira um valor monetário.')
  
  return float(moeda)

