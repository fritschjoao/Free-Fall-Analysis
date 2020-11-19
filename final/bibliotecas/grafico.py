# Biblioteca com as funções de construção do gráfico

import matplotlib.pyplot as plt
import numpy as np

# Função da equação da queda livre
def f(h, g):
    t = np.sqrt( (2*h) / g)
    return t

# Construção do gráfico
def constroiGrafico(aceleracao, alturas, tempos, errors):
    # Lista de pontos para melhor visualização
    x = np.arange(1.75, 2.15, 0.001)

    # PLOTS
    # Reta nova com aceleração ajustada
    nova = plt.plot(x, f(x, aceleracao), label="g = " + str(round(aceleracao, 2)) + "m/s² (ajustada)")
    # Reta padrão com aceleração da gravidade
    padrao = plt.plot(x, f(x, 9.81), label="g = " + "9.81" + "m/s² (padrão)")
    # Error bars
    error_p = plt.errorbar(alturas, tempos, yerr=errors, fmt='o', color='red')

    plt.grid(True)  # Grid no gráfico
    plt.title('GRÁFICO')  # Título
    plt.xlabel('Altura(m)')  # Descrição x = Altura
    plt.ylabel('Tempo(s)')  # Descrição y = Tempo
    plt.legend(loc='upper left')  # Coloca legenda

    plt.savefig('./final/grafico_final.png') # Salva figura
    plt.show()  # Mostrar o gráfico
    