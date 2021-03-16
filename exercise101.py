from datetime import date

def vota(nascimento):
  idade = date.today().year - nascimento
  
  if idade >= 18:
    return f'Com {idade} anos: Voto obrigatório.'
  elif 18 > idade >= 16:
    return f'Com {idade} anos: Voto opcional.'
  elif 16 > idade:
    return f'Com {idade} anos: Não vota.'


ano = int(input('Em que ano você nasceu? '))
print(vota(ano))
