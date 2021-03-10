entrada = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(entrada))
print('Só tem espaços? ', entrada.isspace())
print('É um número? ', entrada.isnumeric())
print('É alfanúmerico? ', entrada.isalnum())
print('Está em maiúsculo? ', entrada.isupper())
print('Está em minúsculo? ', entrada.islower())
print('Está em capitalizada? ', entrada.istitle())
