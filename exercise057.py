sexo = 'none'
while sexo not in 'MF':
  sexo = str(input('Insira o sexo [M/F]: ')).strip().upper()

print('Sexo {} registrado com sucesso.'.format(sexo))
