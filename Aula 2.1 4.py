
temperaturas = [23.4, 25.2, 20.0, 22.1, 27.5, 26.2, 25.8]

for temp in temperaturas:
    if temp>25:
        print('Dia quente', temp)
    else:
        print('Dia agradável ', temp)

#Distribuindo listas de mesmo tamando

gastos = [15.0, 57.0, 83.25, 11.75, 2.0, 52.50, 97.75, 72.25]
essencial = [True, False, False, True, True, True, False, True]

gastos_essencial = 0
gastos_nao_essencial = 0

for i in range(len(gastos)):
    if essencial[i]:
        gastos_essencial += gastos[i]
    else:
        gastos_nao_essencial += gastos[i]

print(gastos)
print(gastos_essencial)
print(gastos_nao_essencial)

# Adicionando itens a uma lista:

itens = []
cont = input('Continuar (S/N)').upper()

while cont == 'S':
    item = input('Novo item: ')
    if item != ' ':
        itens.append(item)
    cont = input('Continuar (S/N)? ').upper()
print(itens)