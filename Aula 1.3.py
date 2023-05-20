class cliente:
    nome = ''
    idade = 0
    endereço = ''
    telefone = ''
class pet:
    nome_pet = ''
    tipo = ''
    idade_pet = 0
    peso = 0
    doença = ''

print('****** CADASTRO DE CLIENTES ******')
cliente.nome = input('Digite o nome do cliente: ')
cliente.idade = int(input('Informe a idade do cliente [Anos]: '))
cliente.endereço = input('Informe o endereço do cliente: ')
cliente.telefone = input('Informe o telefone de contato: ')
print('****** CADASTRO DE PETs ******')
pet.nome_pet = input('Informe o nome do PET: ')
pet.tipo = input('Informe o tipo [espécie] do Pet: ')
pet.idade_pet = input('Informe a idade do Pet em anos: ')
pet.peso = float(input('Informe o peso [Kg]: '))
pet.doença = input('Infome a doença atual do pet: ')

print('*-'*30)
print('O nome do cliente é:', cliente.nome)
print('A idade do cliente é', cliente.idade)
print('O endereço do cliente é: ', cliente.endereço)
print('O telefone de contato é: ', cliente.telefone)
print('*-'*30)
print('O nome do PET é:', pet.nome_pet)
print('O tipo do PET é:', pet.tipo)
print('A idade do PET é', pet.idade_pet)
print('O peso do PET é: ', pet.peso)
print('A doença atual do PET é: ', pet.doença)
print('~-'*30)