from random import randint

while True:
  pc = randint(0,10)
  numero = int(input('Insira um número: '))
  total = numero+pc
  palpite = str(input('A soma será Par ou Ímpar? [P/I]: ')).strip().upper()[0]

  if total%2 == 0:
    if palpite == 'P':
      print(f'Ganhou!\nVocê: {numero}\nComputador: {pc}\nTotal:{total} -> Par!')
    else:
      print(f'Perdeu!\nVocê: {numero}\nComputador: {pc}\nTotal:{total} -> Par!')
      break
  else:
    if palpite == 'I':
      print(f'Ganhou!\nVocê: {numero}\nComputador: {pc}\nTotal:{total} -> Ímpar!')
    else:
      print(f'Perdeu!\nVocê: {numero}\nComputador: {pc}\nTotal:{total} -> Ímpar!')
      break
