# criando um dicionário vazio

dicionario_01 = {} #dicionario vazio
dicionario_02 = dict() # outro dicionário vazio

# estrutura de dados (key:value)
populacao = {'Ceará': 9132078, 'Bahia': 14873064, 'Alagoas': 3337357}

# Imprimirá em tela 'O Ceará possui 9132078 habitantes. '
print('O Ceará possui {} habitantes.'.format(populacao['Ceará']))

# adicionar a população do Maranhão ao dicionário
populacao['Maranhão'] = 7075181

print(populacao)

#Usando um número qualquer como chave (key)

populacao[0] = 10

print(populacao)

#Iterando com dicionários: deve-se fazer a chamada do método/função membro items()

for chave, valor in populacao.items():
    print(f'O {chave} possui {valor} habitantes.')


del populacao[0] #apagando o item 0
print(populacao)

#Além do operador del, também pode ser utilizado o método pop(),
# para excluir uma entrada de um dicionário.

# Caso você tente excluir de novo o elemento indexado pela chave
# 0, como populacao[0].pop(), vai incorrer em um KeyError, que
# é resultante da tentativa de indexação por uma chave que não
# existe no dicionário. Mas, como, então, verificar se um par
# chave:valor existe em um dicionário? Fácil, use o operador
# in e a chave do par como em:

if 0 in populacao:
    populacao[0].pop()

# Este comando resultará em ERRO
# print('O Piauí possui {} habitantes.'.format(populacao['Piauí']))

# O mesmo erro ocorrerá. Então, você pode resolver isso utilizando
# o método get() como na seguinte linha de código:

print('O Piauí possui {} habitantes.'.format(populacao.get('Piauí')))
# No entanto o código acima trás um resultado NONE (vazio)

#RESOLVENDO o problema acima com um if
estado = input('De qual estado você quer saber a população: ')
pop = populacao.get(estado)
if pop == None:
    print('Infelizmente não sabemos informar a população deste estado :(')
else:
    print('{} possui {} habitantes.'.format(estado, pop))

#Para saber as chaves existentes em um dicionário usar o método .keys()

print('Escolha entre os estados: ' + ', '.join(populacao.keys()))

# Onde foi passado a lista resultante de populacao.keys() como parâmetro
# para o método .join(). Esse método, em objetos da classe str , faz com
# que seja concatenado todos os elementos da lista passada como parâmetro,
# usando a string que chamou o método, no caso ', '. Assim, será apresentado
# ao usuário a mensagem a seguir:

print(populacao.values()) #exibindo os valores
print(populacao.keys()) # exibindo as chaves

# demais, também pode apresentar os dados armazenados em um dicionário,
# seguindo uma ordem diferente, e para isso você deve utilizar a função sorted().

# O laço abaixo trás as chaves em ordem alfabética

for estado in sorted(populacao):
    print(f'{estado} possui {populacao[estado]} habitantes.')

print('~~'*30)
#Ordenando os dados pelo valor da população:

for estado in sorted(populacao, key = lambda chave: populacao.get(chave)):
    print(f'{estado} possui {populacao[estado]} habitantes')

# Com isso, o único trecho adicionado é key=lambda chave : população.get(chave)
# e, como resultado, os estados são apresentados na ordem de com menor
# população para o maior. Dessa forma, você consegue compreender o que esse
# trecho faz a mais? Uma dica importante é que key é um parâmetro nomeado
# de sorted, ou seja, está explicitando que a expressão, após o operador =,
# deve ser interpretada como key. Dada essa dica, você entende o que ocorre?
#Esse parâmetro key modifica como as chaves do dicionário serão ordenadas por
# sorted. Assim, após o operador de igualdade (=) foi definida uma função
# lambda. Do lado esquerdo dessa função, tem-se chave, uma variável a qual
# toda chave de populacao será atribuída uma vez, já do lado direito tem-se
# uma expressão com que valor deve ser atribuído a essas chaves para que se
# consiga ordená-las. O valor apresentado é populacao.get(chave), ou seja,
# para cada chave, vai ser utilizado o valor contido no dicionário para
# ordená-la, que é justamente a população do estado, resultado na
# saída a seguir:

# Tópico 2: Conhecendo mais possibilidades com dicionários

# Para resolver a questão proposta anteriormente, fazendo uso de dicionários, utilize caracteres, como chaves e a quantidade de ocorrências na string como valores armazenados em um dicionário. Faça, primeiro, a leitura da string e armazene as informações em um dicionário conforme apresentado no trecho a seguir:

print('~~'*20)
mensagem = input('Digite uma string qualquer: ') # leitura da string
ocorrencias = {} # criação de um dicionário vazio

for letra in mensagem:
    ocorrencias[letra] = ocorrencias.get(letra, 0) + 1  # método get() com dois parâmetros
print(ocorrencias)

#Nesse primeiro trecho, é feito a leitura da string mensagem. Depois, criado o dicionário ocorrências, e, por fim, itera mensagem para extrair todas as letras, para, então, atualizar a quantidade de ocorrências de letra. Você pode ter pensado em um trecho de código maior, em que primeiro testava se a letra já tinha ocorrido ou não, não é? Felizmente, o método get() possibilita um segundo parâmetro, que substitui None, como valor retornado, caso a chave não seja encontrada no dicionário. Assim, na primeira vez que uma letra ocorrer, o valor em ocorrencias[letra] será de 1 e, nas demais vezes, sempre será acrescido de 1 em 1. Por fim, você pode apresentar o resumo das informações, como está nas linhas de código abaixo:

print('A mensagem digitada possui: {} caracteres, sendo {} caracteres únicos.'.format(len(mensagem), len(ocorrencias)))
print('Cada um destes caracteres únicos ocorreu: ')
for letra in sorted(ocorrencias):
    print('\t{} ocorreu {} vezes.'.format(letra, ocorrencias[letra]))
