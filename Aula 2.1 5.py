

produtos = ['aveia', 'sabão em pó', 'manteiga', 'cebola']
quantidades = [1, 1, 1, 1]
menu = """\
Escolha uma opção:
(1) Alterar quantidade
(2) Sair
"""

opcao = int(input(menu))

while opcao != 2:
    if opcao == 1:
        prod = input('Qual produto? ')
        if prod in produtos:
            pos = produtos.index(prod)
            quant = quantidades[pos]
            print(prod, 'tem ', quant, 'unidades')
            nova_quant = int(input('Nova quantidade? '))
            if nova_quant == 0:
                produtos.pop(pos)
                quantidades.pop(pos)
            else:
                quantidades[pos] = nova_quant
        else:
            print('Ops, a lista não contém', prod)
    else:
        print(opcao, 'não é uma opção válida!')
    opcao = int(input(menu))

for i in range(len(produtos)):
    prod = produtos[i]
    quant = quantidades[i]
    print(prod, ' tem ', quant, ' unidades.')