import matplotlib.pyplot as plt

# Classe para representar um livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}, publicado em {self.ano_publicacao}"


# Lista de livros e anos
biblioteca = []
anos = []

# Função para adicionar um livro à biblioteca
def adicionar_livro(titulo, autor, ano_publicacao):
    novo_livro = Livro(titulo, autor, ano_publicacao)
    biblioteca.append(novo_livro)
    anos.append(ano_publicacao)
    print(f"O livro '{titulo}' foi adicionado à biblioteca.")

# Função para listar todos os livros
def listar_livros():
    print("\nLivros na biblioteca:")
    for livro in biblioteca:
        print(livro)


# Adicionando alguns livros
adicionar_livro("Dom Quixote", "Miguel de Cervantes", 1605)
adicionar_livro("Orgulho e Preconceito", "Jane Austen", 1813)
adicionar_livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967)

# Listar todos os livros
listar_livros()

# Criar um gráfico de livros por ano
anos_unicos = sorted(set(anos))  # remove duplicatas e ordena
contagem_por_ano = [anos.count(ano) for ano in anos_unicos]

# Criar um gráfico de linha
plt.plot(anos_unicos, contagem_por_ano, marker='o')
plt.xlabel("Ano de publicação")
plt.ylabel("Número de livros")
plt.title("Distribuição de livros na biblioteca por ano de publicação")

# Adicionar rótulos aos pontos
for i, valor in enumerate(contagem_por_ano):
    plt.text(anos_unicos[i], valor + 0.05, str(valor), ha='center', va='bottom')

plt.grid(True)
plt.show()
