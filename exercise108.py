from exercise107_modulos import moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.cifrao(preco)} é {moeda.cifrao(moeda.metade(preco))}.')
print(f'O dobro de {moeda.cifrao(preco)} é {moeda.cifrao(moeda.dobro(preco))}.')
print(f'Aumentando 10% de {moeda.cifrao(preco)}, temos {moeda.cifrao(moeda.porcentagem(preco, 10))}.')
