redimento = int(input('Qual é o redimento da lata?'))
altura = int(input('Qual é a altura da parede?'))
largura = int(input('Qual é a largura da parede?'))

def caculadora_tinta():
    area = altura * largura
    total = area / redimento
    print(f' Você precisa de {total} latas de tinta')