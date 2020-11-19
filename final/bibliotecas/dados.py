# Biblioteca com as funções de extrações de dados

# Extração do arquivo
def extraiArquivo():
    arquivo = open('./final/arquivos/dados_red.txt', 'r')  # Abre arquivo
    dados = arquivo.read().splitlines() # Divide arquivo
    arquivo.close() # Fecha arquivo
    return dados # Retorna

# Extração dos dados
def extraiDados():
    dados = extraiArquivo() # Chama implícitamente extraiArquivo
    alturas = [] # Cria alturas
    tempos = [] # Cria tempos
    errors = [] # Cria errors

    # Laço para colocar os dados em seus respectivos lugares
    for dado in dados:
        aux = dado.split(' ')
        alturas.append( float(aux[0]) )
        tempos.append( float(aux[1]) )
        errors.append( float(aux[2]) )

    return alturas, tempos, errors  # Retorna referência para as listas ordenadamente