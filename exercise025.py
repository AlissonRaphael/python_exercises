nome = input('Qual é o seu nome completo: ')

print('Seu nome tem Silva? {}.'.format(nome.lower().find('silva') != -1))
