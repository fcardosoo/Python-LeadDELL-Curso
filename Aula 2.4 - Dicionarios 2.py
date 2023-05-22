# Para facilitar sua vida na hora de desenvolver esse sistema de lista telefônica, é possível, em primeiro lugar, criar uma classe Contato para armazenar os dados de todos os contatos e iniciar seu dicionário como está apresentado no seguinte trecho:

class contato:
    nome = ''
    telefone = ''
    email = ''

contatos = {}

# Em contatos, utilize, como chave, as letras A-Z, e cada valor contido no dicionário será uma lista de objetos da classe Contato. Então, desenvolva a célula que lê um novo contato, como está apresentado a seguir:

ctt = contato() # instanciando novo objeto da classe Contato

print('--- Adição de mais um contato --- ') # fazendo leitura dos dados nas 3 linhas a seguir
ctt.nome = input('Digite o nome do contato: ')
ctt.telefone = input('Digite o telefone do contato: ')
ctt.email = input('Digite o email do contato: ')

inicial = ctt.nome[0].upper() # assegurando que a inicial do nome do contato seja maiúscula

if inicial not in contatos: # se nenhum contato com essa inicial foi incluído até o momento
    contatos[inicial] = []  # então inicie a lista de contatos com esta inicial como uma lista vazia
    contatos[inicial].append(ctt)  # adicione o novo contato na lista correta

# Para fazer a apresentação dessa lista telefônica, você precisa de dois laços de repetição aninhados: o primeiro itera em todas as iniciais existentes no dicionário; e o segundo itera em todos os contatos existentes no valor armazenado por uma inicial, como no código abaixo:

for inicial in sorted(contatos): # laço externo itera nas iniciais ordenadas
    print('--- Contatos com a letra {} ---'.format(inicial))
    for ctt in sorted(contatos[inicial], key=lambda c: c.nome):  # laço interno itera nos contatos ordenados
        print('Nome: {}\tTelefone: {}\tEmail:{}'.format(ctt.nome, ctt.telefone, ctt.email))

# Assim, em apenas 4 linhas, você pode apresentar os dados contidos em contatos de forma ordenada. O único trecho diferente do que está acostumado é sorted(contatos[inicial], key=lambda c : c.nome) mas já deve saber que contatos[inicial] é uma lista contendo objetos da classe Contato. Logo, está ordenando essa lista, utilizando o atributo nome como chave para a ordenação. Dessa forma, esse trecho gera resultados a seguir:

# Como você pode perceber, '\t' foi utilizado para separar os campos dos contatos. Utilizando dicionários, listas e strings é possível construir essa lista telefônica de forma bem compacta e organizada! Perceba que aqui foram construídos laços de repetição aninhados, mas, será que é possível fazer o mesmo com dicionários? Acompanhe o vídeo a seguir para descobrir!
