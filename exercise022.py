texto = input('Digite seu nome completo: ')

print('Analisando seu nome...')
print('Seu em maiúsculas é {}'.format(texto.upper()))
print('Seu em minúsculas é {}'.format(texto.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(texto)))
print('O primeiro nome é {} e ele tem {} letras.'.format(texto.split()[0], len(texto.split()[0])))
