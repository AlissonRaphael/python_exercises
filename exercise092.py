from datetime import date

trabalhador = dict()

nome = str(input('Nome: '))
trabalhador['nome'] = nome
nascimento = int(input('Ano de Nascimento: '))
trabalhador['idade'] = date.today().year - nascimento
carteira = int(input('Nº da Carteira de Trabalho [0-Não possui]: '))
trabalhador['carteira'] = carteira if carteira != 0 else 'Não possui'

if carteira != 0:
  contratacao = int(input('Ano de contratação: '))
  trabalhador['contratacao'] = contratacao
  salario = float(input('Valor do salário: R$ '))
  trabalhador['salario'] = salario
  trabalhador['data_aposentadoria'] = 60-(date.today().year - nascimento)+contratacao

print('-'*30)
print(f'- Nome: {trabalhador["nome"]}.')
print(f'- Idade: {trabalhador["idade"]}.')
print(f'- Carteira de Trabalho: {trabalhador["carteira"]}.')
if trabalhador["carteira"] != 'Não possui':
  print(f'- Ano de contratação: {trabalhador["contratacao"]}.')
  print(f'- Valor do salário: R$ {trabalhador["salario"]:.2f}.')
  print(f'- Data de Aposentadoria: {trabalhador["data_aposentadoria"]}.')
