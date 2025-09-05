class Pessoa:
    def __init__(self,nome,idade,cargo):
    self.nome = nome 
    self.idade = idade
    self.cargo = cargo

    def informações(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Cargo: {self.cargo}')
        def promover(self, novo_cargo)

colaborador1 = Pessoa('Ana', 35, 'Assistente Junior')
colaborador2 = Pessoa('Carlos', 45, 'Dev Junior')
