tem_cel=int(input('Qual é a temperatura da carne?'))

if tem_cel < 48:
    print('Cozinhar por mais alguns minutos')
elif tem_cel in range (48, 53):
    print('Selada')
elif tem_cel in range (54, 59):
    print('Ao ponto para o mal')
elif tem_cel in range (60, 64):
    print('Ao ponto')
elif tem_cel in range (65, 70):
    print('Ao ponto para bem')
elif tem_cel in range(71, 75):
    print('Bem passada')
else:
    print('Torrou')