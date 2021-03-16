def notas(*notas, status=False):
  """
    Funcao para analisar as notas e as situacoes dos alunos.
    :param notas: Notas dos alunos [Obrigatorio].
    :param status: Mostra a situacao do aluno [Opcional], Padrao: "False".
    :return: Retorna as informacoes do aluno (dicionario).
  """
  aluno = dict()
  for i, k in enumerate(notas):
    aluno[f"nota{i+1}"] = k

  media = sum(notas)/len(notas)
  aluno['media'] = media
  aluno['total'] = len(notas)

  if status:
    if media >= 7:
      aluno["status"] = 'Boa'
    elif 7 > media >= 5:
      aluno["status"] = 'Razoavel'
    elif 5 > media:
      aluno["status"] = 'Ruim'

  return aluno


print(notas(5, 10, 4, status=True))
help(notas)
