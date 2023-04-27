import numpy as np

def gerar_ação(observação, modelo, pesos):
    """
    Essa função gera uma ação a ser tomada com base na observação do ambiente,
    no modelo de rede neural e nos pesos do modelo.
    Primeiro, a observação é ajustada para ter a dimensão esperada pelo modelo.
    Em seguida, o modelo é usado para realizar a predição dos Q-values (melhores ações)
    para cada ação possível a partir da observação dada e dos pesos do modelo.
    Finalmente, a função retorna a ação com o maior Q-value como uma matriz 
    multidimensional com um único elemento.
    """
    # Ajusta a observação para ter a dimensão esperada pelo modeloo
    observação = np.expand_dims(observação, axis=0)

    # Realiza a predição utilizando o modeloo e os pesos fornecidos
    melhores_ações = modelo(observação, pesos)

    # Seleciona a ação com a maior pontuação mais provável
    ação = np.argmax(melhores_ações)

    # Retorna a ação como uma matriz multidimensional com um único elemento
    return np.reshape(ação, (1,))

    """
    A função criar_pesos_iniciais recebe como entrada um ambiente de aprendizado por reforço,
    o tamanho da população, um modelo já criado e o número máximo de pesos por agente.

    Ela inicializa os pesos do modelo fornecido com valores aleatórios seguindo uma distribuição
    normal, adiciona um ruído gaussiano aos pesos do modelo para diversificar a população e cria
    a população a partir dos pesos do modelo, retornando uma lista de população.

    Essa função é utilizada em algoritmos de otimização por evolução, onde a população
    é usada para encontrar os melhores pesos para o modelo. Os pesos iniciais da população
    são gerados a partir dos pesos do modelo fornecido, mas com pequenas alterações aleatórias,
    o que permite explorar mais o espaço de busca de soluções e aumentar as chances de encontrar um 
    bom conjunto de pesos para o modelo.

    A função limita a quantidade de pesos por agente a um tamanho máximo definido pela variável max_peso_por_agente.
    Caso o número de pesos de um agente seja menor que o tamanho máximo, a função adiciona zeros ao final do vetor
    de pesos para preencher até o tamanho máximo.
    """

def criar_pesos_iniciais(tamanho_da_população):

    # Calcula a quantidade de pesos que cada indivíduo terá
    quantidade_de_pesos = 10

    população = np.random.randn(tamanho_da_população, quantidade_de_pesos)

    return população