qtd_maioridade = qtd_homens = qtd_mulheres_menoridade = 0

while True:
  print('---- Cadastrar uma pessoa ----')
  idade = int(input('Insira a idade: '))
  sexo = str(input('Insira o sexo [M/F]: ')).strip().upper()[0]

  if idade >= 18:
    qtd_maioridade += 1
  
  if sexo == 'M':
    qtd_homens += 1

  if sexo == 'F' and idade < 20:
    qtd_mulheres_menoridade += 1

  opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()
  if opcao == 'N':
    break

print(f'Total de pessoas maiores de 18 anos: {qtd_maioridade}')
print(f'Quantidade de homens cadastrados: {qtd_homens}')
print(f'Quantidade de mulheres com menos de 20 anos: {qtd_mulheres_menoridade}')
