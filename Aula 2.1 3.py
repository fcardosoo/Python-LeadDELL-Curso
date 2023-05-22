# Adicionando itens a uma lista

item = []
print(f'mostrando a lista item: {item}')

if not 'farinha' in item:
    item.append('farinha')
print(f'Mostrando após "if": {item}')

print('~-'*20)
compras = []
itens = 'ovos'
if not itens in compras:
    compras.append(itens)
print(f'Itens da lista de compras: {compras}')
print('~-'*20)

listac = ['farinha', 'ovo', 'fermento']
print(listac)
ingrediente = 'sal'

if listac.count(ingrediente):
    listac.append(ingrediente)
print(listac)