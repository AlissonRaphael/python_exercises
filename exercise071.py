print('---- Caixa eletrônico ----')

valor = float(input('Quanto deseja sacar? R$ '))
qtd_100 = qtd_50 = qtd_25 = qtd_10 = qtd_5 = qtd_2 = qtd_1 = qtd_05 = qtd_025 = 0

while True:
  if valor >= 100:
    qtd_100 += 1
    valor -= 100
  elif 100 > valor >= 50:
    qtd_50 += 1
    valor -= 50
  elif 50 > valor >= 25:
    qtd_25 += 1
    valor -= 25
  elif 25 > valor >= 10:
    qtd_10 += 1
    valor -= 10
  elif 10 > valor >= 5:
    qtd_5 += 1
    valor -= 5
  elif 5 > valor >= 2:
    qtd_2 += 1
    valor -= 2
  elif valor < 2:
    break

print(f'Total de {qtd_100} cédulas de R$ 100.')
print(f'Total de {qtd_50} cédulas de R$ 50.')
print(f'Total de {qtd_25} cédulas de R$ 25.')
print(f'Total de {qtd_10} cédulas de R$ 10.')
print(f'Total de {qtd_5} cédulas de R$ 5.')
print(f'Total de {qtd_2} cédulas de R$ 2.')
