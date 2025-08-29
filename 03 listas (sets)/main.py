funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sofia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sofia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

# Lista01 - quem tem carro e trabalha no turno da noite
lista1 = set(tem_carro).intersection(turno_noite)
print("Lista01:", lista1)

# Lista02 - quem tem carro e trabalha no turno do dia
lista2 = set(tem_carro).intersection(turno_dia)
print("Lista02:", lista2)

# Lista03 - quem é funcionário e tem carro
lista3 = set(funcionarios).intersection(tem_carro)
print("Lista03:", lista3)
