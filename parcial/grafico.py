# Programa do Gráfico

import matplotlib.pyplot as plt
import numpy as np

# Classe para melhor organização do programa
class Grafico:
    # Construtor (VÁRIAVEIS PRINCIPAIS)
    def __init__(self):
        self.dados = [] # Lista que extrai os dados "brutos"
        self.x_alturas = [] # Lista dos xs do gráfico que representa as alturas
        self.y_tempos = [] # Lista dos ys do gráfico que representa os tempos
        self.yerror_dp = [] # Lista dos desvios padrões que representará os 'erros'

    # Extrai os dados do arquivo na lista dados, cada linha do arquivo é um elemento da lista
    def extraiArquivo(self):
        arquivo = open('./parcial/dados/arq_saida.txt', 'r') # Abre arquivo
        self.dados = arquivo.read().splitlines() # Divide as linhas
        arquivo.close() # Fecha arquivo

    # Extrai os dados da lista dados para suas respectivas listas
    def extraiDados(self):
        # Para cada linha existe três informações : (altura / tempo / desvio padrão)
        for dado in self.dados:
            aux = dado.split(' ')  # Divide a linha em uma nova lista que separa essas três informações
            self.x_alturas.append( float(aux[0]) ) # Lista x_alturas recebe a altura
            self.y_tempos.append( float(aux[1]) ) # Lista y_tempos recebe o tempo
            self.yerror_dp.append( float(aux[2]) ) # Lista yerror_dp recebe o desvio padrão
        # Repete para todas as linhas

    # Função gravidade
    def f(self, x):
        return np.sqrt( (2*x) / 9.81)
    
    # Constrói o gráfico a partir das informações já obtidas
    def constroiGrafico(self):
        # GRAVIDADE
        x = np.arange(1.75, 2.15, 0.001)  # Lista de pontos para melhor visualização
        gravidade = 9.81  # Gravidade
        plt.plot(x, self.f(x))  # Constrói curva

        # ERROR BAR
        plt.errorbar(self.x_alturas, self.y_tempos, yerr=self.yerror_dp, fmt='o', color='red')  # Construtor
        
        plt.title('GRÁFICO')  # Título
        plt.xlabel('Altura(m)')  # Descrição x = Altura
        plt.ylabel('Tempo(s)')  # Descrição y = Tempo
        
        plt.savefig('./parcial/grafico_parcial.png') # Salva figura
        plt.show()  # Mostrar o gráfico

# Função principal "chamadora"
def inicia():
    #Cria objeto Gráfico
    grafico = Grafico()

    grafico.extraiArquivo()
    grafico.extraiDados()
    grafico.constroiGrafico()

# Inicia a execução do programa
inicia()
