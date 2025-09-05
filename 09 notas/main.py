# Função para adicionar notas
def cadastrar_notas():
    notas = []  # Lista para armazenar as notas
    while True:
        try:
            nota = float(input("Digite a nota do aluno (ou -1 para finalizar): "))
            if nota == -1:  # Condição de parada
                break
            if 0 <= nota <= 10:  # Validação da nota
                notas.append(nota)
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número.")
    return notas

# Função para calcular a média
def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

# Função para determinar a situação do aluno
def determinar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Função para exibir o relatório final
def exibir_relatorio(notas, media, situacao):
    print("\n=== Relatório Final ===")
    print(f"Notas inseridas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

# Programa principal
def main():
    print("=== Sistema de Gestão de Notas ===")
    
    # Cadastro de notas
    notas = cadastrar_notas()
    
    # Cálculo da média
    media = calcular_media(notas)
    
    # Determinação da situação
    situacao = determinar_situacao(media)
    
    # Exibição do relatório final
    exibir_relatorio(notas, media, situacao)

# Executar o programa
main()
