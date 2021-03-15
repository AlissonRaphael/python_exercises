aluno = dict()

nome = str(input('Nome: '))
media = float(input('Média: '))

aluno['nome'] = nome
aluno['media'] = media
if media < 5:
  aluno['status'] = 'Reprovado!'
elif 5 <= media < 7:
  aluno['status'] = 'Recuperação!'
else:
  aluno['status'] = 'Aprovado!'

print(f'Nome: {aluno["nome"]}.')
print(f'Média: {aluno["media"]}.')
print(f'Situação: {aluno["status"]}')
