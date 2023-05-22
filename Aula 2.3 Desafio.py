

presentes = {'cadeira', 'cafeteira', 'caneca', 'escumadeira',
             'espanador', 'espátula', 'estante', 'faqueiro',
             'frigideira', 'funil', 'halter', 'liquidificador',
             'notebook', 'panela', 'peneira', 'playstation','rádio',
             'smartphone', 'sofá', 'tablet', 'teclado', 'televisão',
             'vassoura', 'webcam', 'xbox'}

loja1 = {'cadeira', 'cafeteira', 'caneca', 'escumadeira', 'estante',
         'frigideira', 'funil', 'liquidificador', 'notebook',
         'panela', 'playstation', 'smartphone', 'teclado',
         'televisão'}

loja2 = {'cafeteira', 'escumadeira', 'espanador', 'frigideira',
         'funil', 'halter', 'peneira', 'playstation', 'sofá',
         'tablet', 'televisão', 'vassoura', 'webcam', 'xbox'}

loja3 = {'caneca', 'escumadeira', 'espanador', 'espátula',
         'estante', 'frigideira', 'halter', 'playstation',
         'rádio', 'smartphone', 'sofá', 'teclado', 'televisão',
         'vassoura', 'xbox'}

loja4 = {'caneca', 'escumadeira', 'espanador', 'espátula',
         'estante', 'frigideira', 'halter', 'playstation',
         'rádio', 'smartphone', 'sofá', 'teclado', 'televisão',
         'vassoura', 'xbox'}

q1 = loja1.union(loja2, loja3, loja4)
print(f'1. Produtos oferecidos em alguma loja: \n{q1}')
print(' ')
q2 = loja1.intersection(loja2, loja3, loja4)
print(f'2. Produtos em todas as lojas:\n{q2}')
print(' ')
q3 = presentes.difference(loja1, loja2, loja3, loja4)
print(f'3. Produtos não encontrados: \n{q3}')
print(' ')
q4l1 = loja1.difference(loja2, loja3, loja4)
q4l2 = loja2.difference(loja1, loja3, loja4)
q4l3 = loja3.difference(loja1, loja2, loja4)
q4l4 = loja4.difference(loja1, loja2, loja3)
print(f'Produtos exclusivos da loja 1: {q4l1}\n'
      f'Produtos exclusivos da loja 2: {q4l2}\n'
      f'Produtos exclusivos da loja 3: {q4l3}\n'
      f'Produtos exclusivos da loja 4: {q4l4}')

pi12 = presentes.intersection(loja1, loja2)
pi13 = presentes.intersection(loja1, loja3)
pi14 = presentes.intersection(loja1, loja4)
pi23 = presentes.intersection(loja2, loja3)
pi24 = presentes.intersection(loja2, loja4)
pi34 = presentes.intersection(loja3, loja4)

print(f'As lojas 1 e 2 possuem {len(pi12)} itens da lista.\n'
      f'As lojas 1 e 3 possuem {len(pi13)} itens da lista.\n'
      f'As lojas 1 e 4 possuem {len(pi14)} itens da lista.\n'
      f'As lojas 2 e 3 possuem {len(pi23)} itens da lista.\n'
      f'As lojas 2 e 4 possuem {len(pi24)} itens da lista.\n'
      f'As lojas 3 e 4 possuem {len(pi34)} itens da lista.')