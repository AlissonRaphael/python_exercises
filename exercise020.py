from random import shuffle

alunoI = input('Digite o aluno I: ')
alunoII = input('Digite o aluno II: ')
alunoIII = input('Digite o aluno III: ')
alunoIV = input('Digite o aluno IV: ')
ordem = [alunoI,alunoII,alunoIII, alunoIV]
shuffle(ordem)

print('A ordem de apresentação será')
print(ordem)
