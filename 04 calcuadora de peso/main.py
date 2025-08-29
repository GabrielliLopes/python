altura = float(input('Qual é a sua altura em cm: '))
peso = float(input('Qual é a seu peso em kg: '))

IMC = peso / (altura/100)**2
print(IMC)

if IMC < 18.5:
    print('Você é magro')
elif IMC >= 18.5 and IMC < 24.9:
    print('Normal')
elif IMC >= 25.0 and IMC < 29.9:
    print('Sobrepeso')
elif IMC >= 30.0 and IMC < 39.9:
    print('Obesidade')
else:
    print('Obesidade Grave')