def potencia(base, expoente=2):
    return base ** expoente

user_number = int(input('Digite o numero base: '))
user_expoente = int(input('Digite um expoente(defalt 2): '))

if user_expoente:
    print(f'O resultado é: {potencia(user_number, int(user_expoente))}')
else:
    print('f O resultado é: {potencia(user_number)}')