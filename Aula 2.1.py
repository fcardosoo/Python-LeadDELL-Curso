
gastos = [23.5, 45.6, 5.24, 2.36, 99.49]

gastos[2] = 3.29
print(gastos)

gastos[-2] = 1.75
print(gastos)

# Remoção de variáveis

del gastos[1]
print(gastos)

# Adição de variáveis

gastos.insert(2, 77.7)
print(gastos)

# FATIAMENTO

numeros = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numeros)
print('fatiando numeros [2:5]:', numeros[2:5])
print('fatiando numeros [:5]:', numeros[:5])
print('fatiando numeros [5:] é similar a [5:11]: ', numeros[5:])

print('Usando o len para contar os elementos de numeros: ', len(numeros))

print('Mostrando uma lista de trás para frente [::-1]:', numeros[::-1])
print('Mostrando numeros pulando de 2 em 2...[0:11:2]:', numeros[0:11:2])
print('Mostrando lista com numero inicial e final igual [4:4] que resulta em lista vazia: ', numeros[4:4])

casas_pares = [216, 220, 222, 268, 270]
print('Casas pares: ',casas_pares)

print('adicionando [232, 240, 252] na ordem da lista anterior')
casas_pares = casas_pares[:3] + [232, 240, 252] + casas_pares[3:]
print(casas_pares)

# OUTROS MÉTODOS DE ADICIONAR FATIAMENTOS

print('~-'*30)
print(casas_pares)
print('Adicionar 276 ao final com o comando casas_pares.append(276)')
casas_pares.append(276)
print(casas_pares)
print('Adicionar 280 ao final com o comando casas_pares+=[280]')
casas_pares+=[280]
print(casas_pares)

print(' ')
print('~-'*30)
print(' ')

print(casas_pares)
print('Adicionar vários ao final com o comando casas_pares.extend([282, 284])')
casas_pares.extend([282, 284])
print(casas_pares)
print('Adicionar vários ao final com o comando casas_pares+=[286, 288]')
casas_pares += [286, 288]
print(casas_pares)

print(' ')
print('~-'*30)
print(' ')

print(casas_pares)
print('Adicionar ao meio com o comando casas_pares.insert(3, 250)')
casas_pares.insert(3, 250)
print(casas_pares)
print('Adicionar ao meio com o comando casas_pares=casas_pares[:2] + [250] + casas_pares[2:]')
casas_pares = casas_pares[:2] + [250] + casas_pares[2:]
print(casas_pares)

print(' ')
print('~-'*30)
print(' ')

print(casas_pares)
print('Remover ao final com o comando casas_pares.pop()')
casas_pares.pop()
print(casas_pares)
print('Remover ao final com o comando casas_pares=casas_pares[:-1]')
casas_pares = casas_pares[:-1]
print(casas_pares)

print(' ')
print('~-'*30)
print(' ')

print(casas_pares)
print('Remover do meio com o comando casas_pares.pop(3)')
casas_pares.pop(3)
print(casas_pares)
print('Remover do meio com o comando casas_pares=casas_pares[:3] + casas_pares[4:]')
casas_pares = casas_pares[:3] + casas_pares[4:]
print(casas_pares)
