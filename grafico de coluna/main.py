import matplotlib.pyplot as plt

#dados
x = [1,2,3,4,5]
y = [2,4,1,3,5]

#criar um grafico de linha
plt.bar(x,y)

#adicionar eixos
plt.xlabel('Eixo X')
plt.xlabel('Eixo Y')

#adicionar um titulo ao grafico
plt.title('Exemplo de Gráfico de Linha')

#mostrar o gráfico
plt.show