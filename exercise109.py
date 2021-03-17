from exercise107_modulos import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.cifrao(preco)} é {moeda.metade(preco, True)}.')
print(f'O dobro de {moeda.cifrao(preco)} é {moeda.dobro(preco, True)}.')
print(f'Aumentando 10% de {moeda.cifrao(preco)}, temos {moeda.porcentagem(preco, 10, True)}.')
