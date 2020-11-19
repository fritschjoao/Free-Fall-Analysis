# Programa "main"

import bibliotecas.dados as dados
import bibliotecas.ajusta as ajusta
import bibliotecas.grafico as grafico

# Inicia programa
def inicia():

    # VARIÁVEIS
    alturas = []  # Alturas extraídas do arquivo
    tempos = []  # Tempos extraídos do arquivo
    errors = []  # Errors extraídos do arquivo
    aceleracao = 0 # Aceleração descoberta no processo
    x = [] # Lista linearizada de tempos
    y = [] # Lista linearizada de alturas

    # Extrai dados a partir da biblioteca "dados"
    alturas, tempos, errors = dados.extraiDados()
    
    # Lineariza
    x, y = ajusta.lineariza(tempos, alturas)

    # Ajusta a função linearizada e descobre a aceleração ideal
    aceleracao = ajusta.resolve(x, y)
    print("ACELERAÇÃO AJUSTADA: " + str(aceleracao))
    
    # Constrói o gráfico
    grafico.constroiGrafico(aceleracao, alturas, tempos, errors)


inicia()