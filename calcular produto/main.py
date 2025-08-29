porções = int(input('Quantas porções o produto tem?: '))
dias = int(input('Quantas porçoes voce usa por dia?: '))

dias = porções / dias
print(f' O produto irá durar {dias:.0f} dias')
print(f' O produto irá durar {int(dias)} dias')