from datetime import date

total_idade = 0
maior_idade_homem = 0
maior_idade_homem_nome = 0
quantidade_mulher_menoridade = 0

for i in range(1,5):
  print('---- Insira os dados da {}ª pessoa ----')
  nome = str(input('Nome: ')).strip()
  idade = int(input('Idade: '))
  sexo = str(input('Sexo [M/F]: ')).strip().upper()

  total_idade += idade

  if i == 1 and sexo == 'M' or idade > maior_idade_homem:
    maior_idade_homem = idade
    maior_idade_homem_nome = nome

  if sexo == 'F' and idade < 20:
    quantidade_mulher_menoridade += 1

print('A média de idade do grupo é {} anos.'.format(total_idade/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem,maior_idade_homem_nome))
print('No grupo tem {} mulher(es) menores de 20 anos.'.format(quantidade_mulher_menoridade))
