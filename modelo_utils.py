from tensorflow.keras import initializers
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
    Ela inicializa os pesos do modelo fornecido com valores aleatórios seguindo uma distribuição
    normal, adiciona um ruído gaussiano aos pesos do modelo para diversificar a população e cria
    a população a partir dos pesos do modelo, retornando uma lista de população.
    """

def criar_pesos_iniciais(tamanho_da_população, modelo):
    print("Criar pesos iniciais")
    print(modelo.count_params())

    # Define a quantidade de pesos que cada indivíduo terá
    quantidade_de_pesos = modelo.count_params()
    
    initializer = initializers.HeUniform()
    população = initializer((tamanho_da_população, quantidade_de_pesos))
    print(população)
    print("Criar pesos iniciais")
    return população