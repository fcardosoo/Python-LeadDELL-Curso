'''
nome = 'Ana Maria Freitas'

letras = set(nome)
print(letras)

nome_tratado = nome.replace(" ", "").upper()
letras = set(nome_tratado)

print(letras)
'''

# Lista de cidades onde serão realizadas partidas consecutivas

cidades = ['Manaus', 'Brasília', 'Fortaleza', 'Manaus', 'Rio de Janeiro', 'Brasília',
           'Fortaleza', 'Natal', 'Belo Horizonte', 'Fortaleza', 'Cuiabá', 'Rio de Janeiro']

# Em quais cidades haverá ao menos UMA partida?

print(set(cidades))
print(len(cidades))

hashtags = (
            '#sol', '#litoral', '#mar', '#natureza', '#viagem', '#natureza',
            '#curtição', '#descanso', '#férias', '#viagem', '#viagem', '#litoral'
)

print(set(hashtags))
print('~~'*30)

lista_animais = ['papagaio', 'onça', 'lobo', 'gavião', 'baleia']
print('lobo' in lista_animais)

conjunto_animais = {'papagaio', 'onça', 'lobo', 'gavião', 'baleia'}
print('lobo' in conjunto_animais)

print('~~'*30)
for animal in conjunto_animais:
    print(animal)

print('~~'*30)

cid = ['Manaus', 'Brasília', 'Fortaleza', 'Manaus', 'Rio de Janeiro',
       'Brasília', 'Fortaleza', 'Natal', 'Belo Horizonte', 'Fortaleza',
       'Cuiabá', 'Rio de Janeiro']
cida = sorted(set(cid))
print(cida)

print('~~'*30)
mult_2 = {0, 2, 4, 6, 8, 10, 12}
mult_3 = {0, 3, 6, 9, 12}

print('União dos conjuntos com o operador "|" mult_2|mult_3')
Uniao = mult_2|mult_3
print(Uniao)

print('União dos conjuntos com método mult_2.union(mult_3)')
Uniao2 = mult_2.union(mult_3)
print(Uniao2)
print('~~'*30)

print('Intersecção dos conjuntos com operador "&" mult_2 & mult_3')
Intersec = mult_2 & mult_3
print(Intersec)

print('Intersecção dos conjuntos com método mult_2.intersection(mult_3)')
Interserc2 = mult_2.intersection(mult_3)
print(Interserc2)
print('~~'*30)

print('Diferença dos conjuntos 2 - 3 com operador "-" mult_2 - mult_3')
dif = mult_2 - mult_3
print(dif)
print('Diferença dos conjuntos com método mult_3.difference(mult_2)')
dif2 = mult_3.difference(mult_2)
print(dif2)

print('~~'*30)

pares_ate10 = {0, 2, 4, 6, 8, 10}
ate10 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print('~~'*30)

modelos = {'clio', 'gol', 'palio', 'prisma'}
print(modelos)
modelos.add('fox')
print('Adicionando "fox" ao conjundo com o método "modelos.add("fox")')
print(modelos)
print('Adicionando vários modelos com o método "modelos.update()"')
modelos.update({'fox', 'duster', 'kwid'})
print(modelos)

print('para remover um item é possível usar os métodos \n'
      'remove ou discart, porém o método REMOVE gera um \n'
      'erro KeyError se o item a ser removido não existir\n'
      'na lista... o método DISCARD não gera erro.')
print('removendo "gol" com com o método REMOVE')
modelos.remove('gol')
print(modelos)
print('removendo fox com o método DISCARD')
modelos.discard('fox')
print(modelos)

print('Para remover vários itens usar o método:\n'
      'difference_update ... removendo prisma e clio')
modelos.difference_update('prisma', 'clio')
print(modelos)