frase = str(input('Digite uma frase: '))

inverso = ''
for index in range(len(frase), 0, -1):
  inverso += frase[index-1]

print(inverso)

if frase == inverso:
  print('Trata-se de um palíndromo!')
