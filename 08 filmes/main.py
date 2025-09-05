# Filmes para classificação
filmes = ['Procurando Nemo', 'Divertida Mente', 'Os Incríveis', 'Toy Story', 'O Rei Leão']

# Dicionário para armazenar as classificações
notas = {}

# Mensagem de boas-vindas
print('Bem-vindo à classificação de filmes!')
print('Você tem cinco filmes para classificar.')
print('Digite "0" a qualquer momento para parar.\n')

# Loop para iterar sobre cada filme na lista
for filme in filmes:
    while True:
        classificacao = input(f'Como você classificaria "{filme}" de 1 a 5? (ou 0 para parar): ')

        # Verifica se o usuário deseja parar
        if classificacao == '0':
            print('Que pena que você não irá classificar mais os filmes.')
            break

        # Converte a classificação para número inteiro
        try:
            classificacao = int(classificacao)
        except ValueError:
            print('Por favor, digite um número válido.')
            continue

        # Verifica se a classificação está dentro do intervalo válido
        if classificacao < 1 or classificacao > 5:
            print('Por favor, digite uma classificação válida de 1 a 5.')
        else:
            # Armazena a classificação
            notas[filme] = classificacao
            print(f'Você classificou "{filme}" com {classificacao} estrelas.\n')
            break

# Verifica se o usuário classificou pelo menos um filme
if notas:
    # Encontra a maior nota
    maior_nota = max(notas.values())
    # Lista todos os filmes que receberam a maior nota
    filmes_mais_gostados = [filme for filme, nota in notas.items() if nota == maior_nota]

    print('Obrigada por classificar os filmes!')
    if len(filmes_mais_gostados) == 1:
        print(f'O filme que você mais gostou foi: "{filmes_mais_gostados[0]}" com {maior_nota} estrelas.')
    else:
        print(f'Os filmes que você mais gostou foram: {", ".join(filmes_mais_gostados)} com {maior_nota} estrelas cada.')
else:
    print('Você não classificou nenhum filme.')
