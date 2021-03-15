matriz = []
vetor = []
pares = coluna = linha = 0

for i in range(0, 3):
  for k in range(0, 3):
    n = int(input(f'Insira um valor para [{i}][{k}]: '))
    vetor.append(n)

    if n%2 == 0:
      pares += n

    if k == 2:
      coluna += n

    if i == 1:
      linha += n

  matriz.append(vetor[:])
  vetor.clear()

print(f'A soma dos valores pares é: {pares}.')
print(f'A soma dos valores da terceira coluna é: {coluna}.')
print(f'A soma dos valores da segunda linha é: {linha}.')
