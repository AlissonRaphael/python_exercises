dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos quilometros rodados? '))
valor = dias*60 + km*0.15

print('O total a pagar é R$ {:.2f}'.format(valor))
