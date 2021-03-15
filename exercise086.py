matriz = []
vetor = []

for i in range(0, 3):
  for k in range(0, 3):
    n = int(input(f'Insira um valor para [{i}][{k}]: '))
    vetor.append(n)
  
  matriz.append(vetor[:])
  vetor.clear()

for linha in matriz:
  for termo in linha:
    print(f'[{termo:<2}] ', end='')
  
  print()
