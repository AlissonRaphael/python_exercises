num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
num3 = float(input('Digite o terceiro valor: '))

menor = num1
maior = num1

if num2 <= menor:
  menor = num2
else:
  maior = num2

if num3 <= menor:
  menor = num3
else:
  maior = num3

print('O menor valor é {:.0f}.'.format(menor))
print('O maior valor é {:.0f}.'.format(maior))
