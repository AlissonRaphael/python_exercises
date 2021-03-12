nome = input('Digite seu nome: ').strip()

print('A letra "A" aparece {} vezes na frase.'.format(nome.lower().count('a')))
print('A primeira letra "A" aparece na posição {}.'.format(nome.lower().find('a')+1))
print('A ultima letra "A" aparece na posição {}.'.format(nome.lower().rfind('a')+1))
