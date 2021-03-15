aluno = list()
alunos = list()

while True:
  nome = str(input('Nome: ')).strip()
  nota1 = float(input('Nota I: '))
  nota2 = float(input('Nota II: '))
  media = (nota1+nota2)/2

  aluno.append(nome)
  aluno.append(nota1)
  aluno.append(nota2)
  aluno.append(media)

  alunos.append(aluno[:])
  aluno.clear()

  opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
  if opcao == 'N':
    break

print(f'{"ID":<4}{"Nome":<25}{"Média":<6}')
print('-'*35)
for index, aluno in enumerate(alunos):
  print(f'{index:<4}{aluno[0]:<25}{aluno[3]:<6}')
print('-'*35)

while True:
  acao = int(input('O que deseja fazer?\n[99] - Encerra execução.\n[id] - ID do aluno para consultar mais informações.\nDigite a opção: '))
  if acao == 99:
    break
  else:
    for index, aluno in enumerate(alunos):
      if acao == index:
        print('-'*40)
        print(f'{"Nome":<15}{"Nota I":<10}{"Nota II":<10}{"Média":<10}')
        print(f'{aluno[0]:<15}{aluno[1]:<10}{aluno[2]:<10}{aluno[3]:<10}')
        print('-'*40)
