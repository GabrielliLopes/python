class Carro:
    def __init__(self, cor, ano):
        self.cor = cor
        self.ano = ano
        self.ligado = False
        self.seta = "desligada"  # seta começa desligada

    def informacoes(self):
        print(f'A cor do carro é {self.cor}')
        print(f'O ano do carro é {self.ano}')
        print(f'O carro está {"ligado" if self.ligado else "desligado"}')
        print(f'A seta está {self.seta}')

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('O carro foi ligado')
        else:
            print('O carro já estava ligado')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print('O carro foi desligado')
        else:
            print('O carro já estava desligado')

    def ligar_seta(self, lado):
        if lado.lower() in ["esquerda", "direita"]:
            self.seta = lado.lower()
            print(f'A seta {self.seta} foi ligada')
        else:
            print("Opção inválida! Use 'esquerda' ou 'direita'.")

    def desligar_seta(self):
        if self.seta != "desligada":
            print(f'A seta {self.seta} foi desligada')
            self.seta = "desligada"
        else:
            print("As setas já estavam desligadas")


# Testando o carro
carro1 = Carro('Preto', 2021)
carro1.informacoes()
carro1.ligar()
carro1.ligar_seta("esquerda")
carro1.ligar_seta("direita")
carro1.desligar_seta()
carro1.desligar()
