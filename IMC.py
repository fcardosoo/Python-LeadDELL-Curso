'''Calcular IMC'''

print('*-'*15)
print('**** Calculadora de IMC ****')
print('*-'*15)

peso = float(input('Digite o seu peso [Kg]: '))
altura = float(input('Digite a sua altura [m]: '))

imc = peso/(altura*altura)

print(f'Seu peso é {peso}Kg e sua altura é {altura}m, seu IMC é {imc:.2f}')