from random import randint

def sortear(qtd):
  numeros = list()
  for i in range(0, qtd):
    numero = randint(0,10)
    numeros.append(numero)

  return numeros


def somar_pares(valores):
  soma = 0
  for valor in valores:
    if valor%2 == 0:
      soma += valor

  return soma


lista = sortear(5)
print(f'Sorteando {len(lista)}: {lista}.')
print(f'A soma dos valores pares da lista é: {somar_pares(lista)}')
