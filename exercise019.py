import random

alunoI = input('Digite o aluno I: ')
alunoII = input('Digite o aluno II: ')
alunoIII = input('Digite o aluno III: ')
alunoIV = input('Digite o aluno IV: ')
escolhido = random.choice([alunoI,alunoII,alunoIII, alunoIV])

print('O aluno escolhido foi {}.'.format(escolhido))
