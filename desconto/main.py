preço = 50 #valor em R$
desconto = 10 #desconto em %

preço = int(input('Digite o valor do produto: '))
desconto = int(input('Digite o desconto a ser aplicado: '))
novo_preço = preço - (preço * desconto / 100)
print(f' O valor do desconto é de R$ {novo_preço}')