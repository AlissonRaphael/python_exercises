pessoa = dict()
pessoas = list()
idade_total = 0

while True:
  print('Cadastrar uma pessoa'.center(40))
  print('-'*40)
  
  nome = str(input('Nome: '))
  pessoa['nome'] = nome
  
  while True:
    sexo = str(input('Nome [M/F]: ')).strip().upper()[0]
    if sexo in 'MF':
      pessoa['sexo'] = 'Masculino' if sexo == 'M' else 'Feminino'
      break
    else:
      print('Inválido! Digite M ou F, para masculino ou feminino.')

  idade = int(input('Idade: '))
  pessoa['idade'] = idade
  idade_total += idade

  pessoas.append(pessoa.copy())
  pessoa.clear()

  opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
  if opcao == 'N':
    break

  print('-'*40)

print(f'A) Temos {len(pessoas)} pessoa(s) cadastradas.')
print(f'B) A média de idade é {idade_total/len(pessoas):.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for pessoa in pessoas:
  if pessoa['sexo'] == 'Feminino':
    print(f'{pessoa["nome"]} ', end='')
print('\nD) Pessoas acima da média de idade: ')
for pessoa in pessoas:
  if pessoa['idade'] >= idade_total/len(pessoas):
    print(f'--- {pessoa["nome"]} de {pessoa["idade"]} anos, sexo {pessoa["sexo"]}.')
