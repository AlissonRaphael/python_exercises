def escreva(msg):
  tamanho = len(msg)+4
  print('-'*tamanho)
  print(f'{msg}'.center(tamanho))
  print('-'*tamanho)


escreva('Curso de Python')
escreva('Aula de definições de funçoes')
