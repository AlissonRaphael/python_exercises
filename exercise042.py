seq1 = float(input('Tamanho do segmento I: '))
seq2 = float(input('Tamanho do segmento II: '))
seq3 = float(input('Tamanho do segmento III: '))

if seq2 + seq3 > seq1 and seq1 + seq3 > seq2 and seq1 + seq2 > seq3:
  
  if seq1 == seq2 == seq3:
    print('Forma um triângulo equilátero.')
  elif seq1 == seq2 or seq1 == seq3 or seq2 == seq3:
    print('Forma um triângulo isósceles.')
  
else:
  print('Não forma um triângulo.')
