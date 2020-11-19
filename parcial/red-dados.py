# Programa de Redução dos Dados

import math

# Classe para melhor organização do programa
class Dados:
    # Construtor (VÁRIAVEIS PRINCIPAIS)
    def __init__(self):
        self.tempos = []  # Lista de tempos extraídos
        self.altura = 0  # Altura extraída
        self.media_tempo = 0  # Média dos tempos calculada
        self.desvio_padrao = 0  # Desvio Padrão calculado
        self.variancia = 0  # Variancia usada para cálculo do desvio padrao
        self.linhas = []  # Linhas a serem escritas no arquivo de saída


    # Calcula a média dos tempos
    def calculaMedia(self):
        somatorio = 0  # Somatório inicia em zero
        n = len(self.tempos)  # Número de elementos na lista tempos
        media = 0  # Media inicia em zero

        # Realiza o somatório de todos tempos da lista
        for tempo in self.tempos:
            somatorio += tempo

        # Cálculo final da média de acordo com a fórmula principal
        self.media_tempo = (somatorio / n)


    # Calcula a variância (usada para cálculo do desvio padrão)
    def calculaVariancia(self):
        somatorio = 0  # Somatório inicia em zero
        n = len(self.tempos)  # Número de elementos na lista tempos
        variancia = 0  # Variancia inicia em zero

        # Realiza o somatório de (tempo-media)² (de acordo com a fórmula)
        for tempo in self.tempos:
            item = abs(tempo-self.media_tempo)  # Valor absoluto do cálculo é usado
            somatorio += math.pow(item, 2)

        # Cálculo final da variância de acordo com a fórmula principal
        self.variancia = (somatorio / (n-1))


    # Calcula o desvio padrão a partir da variância já calculada
    def calculaDesvioPadrao(self):
        # Desvio padrao = raiz da variância
        self.desvio_padrao = math.sqrt(self.variancia)


    # Extrai os tempos do arquivo "n" passado
    def extraiTempos(self, n):
        # Se n = 1, abre arquivo a1, assim por diante...
        arquivo = open('./dados/a'+str(n)+'.txt', 'r')

        # Primeira linha do arquivo é sempre a altura
        # O arquivo retorna o tipo string, por isso precisa transformar em float
        self.altura = float(arquivo.readline())

        # Demais linhas são os tempos
        self.tempos = arquivo.read().splitlines()

        # Assim como na altura, precisa-se transformar em float
        self.tempos = [float(i) for i in self.tempos]

        # Fecha o arquivo
        arquivo.close()


    # Adiciona mais uma linha a lista linhas no formato (altura / tempo / desvio padrao)
    def completaLinhas(self):
        # Obs: round usado para arredondar casas decimais
        self.linhas.append(str( round(self.altura, 5) ) + ' ' 
                         + str( round(self.media_tempo, 5) ) + ' ' 
                         + str( round(self.desvio_padrao, 5) ) + '\n')


    # Preenche o arquivo de saida com tres colunas : altura / tempo / desv. padrao
    def preencheArquivoSaida(self):

        # Abre o arquivo de saída
        arquivoSaida = open("./dados/arq_saida.txt", "w")

        # Transforma cada elemento da lista 'linhas' em uma linha do arquivo
        arquivoSaida.writelines(self.linhas)

        # Fecha o arquivo
        arquivoSaida.close()


# Função com o laço principal para execução de todos os 5 arquivos
def inicia():
    #Cria objeto dados
    dados = Dados()

    # n de 1 até 5
    for n in range(1,6):
        dados.extraiTempos(n)
        dados.calculaMedia()
        dados.calculaVariancia()
        dados.calculaDesvioPadrao()
        dados.completaLinhas()
        dados.preencheArquivoSaida()

# Inicia a execução do programa
inicia()




    










