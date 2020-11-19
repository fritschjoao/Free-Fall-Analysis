# Biblioteca com as funções de ajuste de funções

import numpy as np

# Função de linearização da equação da queda livre
def lineariza(tempos, alturas):
    x = [item**2 for item in tempos] # x = t²
    y = alturas # y = h

    return x, y

# Ajusta a função lineariza e devolve a aceleração nova
def resolve(x, y):

    # Se as listas tiverem tamanho diferente, n faz nada
    if len(x) != len(y):
        return
    
    # n usado nas somas (n = tamanho das listas)
    n = len(x)

    # Somatórios
    somX = somX2 = somY = somXY = 0
    
    # Aplica os somatórios para n
    for j in range(n):
        somX += x[j]
        somY += y[j]
        somX2 = x[j]**2
        somXY = x[j]*y[j]

    # Coeficientes
    d = float(n*somX2 - somX**2)  # denominador de ambas fórmulas
    a = (n*somXY - somX*somY)/d  # a = aceleracao/2, logo aceleracao = a*2
    b = (somX2*somY - somXY*somX)/d # b nao é usado nesse caso

    aceleracao = 2*a  # resultado final

    return aceleracao