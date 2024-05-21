# Função para criar uma matriz 4x4 com valores padrão
def criar_matriz():
    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            # Pode-se adicionar valores desejados para a matriz aqui
            # Neste exemplo, estamos preenchendo com zeros
            linha.append(0)
        matriz.append(linha)
    return matriz

# Função para exibir a matriz na tela
def exibir_matriz(matriz):
    for linha in matriz:
        print(linha)

# Criar uma matriz 4x4
matriz_4x4 = criar_matriz()

# Exibir a matriz
exibir_matriz(matriz_4x4)