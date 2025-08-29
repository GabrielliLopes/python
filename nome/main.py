nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
fruta_favorita = input('Qual é a sua fruta favorita? ')

# sem o f-string
print('Olá', nome + ', você tem', idade, 'anos de idade')

# com o f-string
print(f'Olá {nome}, você tem {idade} anos de idade e a sua fruta favorita é {fruta_favorita}')
