numeros = ('zero', 'um', 'dois', 'três','quatro', 'cinco', 'seis', 'sete', 'oito',
  'nove','dez','onze', 'doze', 'treze', 'quatorze','quinze', 'dezesseis',
  'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
  numero = int(input('Digite um número entre 0 e 20: '))

  if 0 <= numero <= 20:
    print(f'O número digitado em extenso é: {numeros[numero]}.')
    break

  print('Inválido!')
