from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D

def criar_modelo(ambiente):
    """
    Esta função cria um modelo de rede neural para ser usado em um ambiente de aprendizado
    por reforço. O modelo é construído com as seguintes camadas:

    Três camadas convolucionais com 32, 64 e 64 filtros, respectivamente, tamanhos de kernel
    de 8, 4 e 3, respectivamente, funções de ativação ReLU e passos de 4, 2 e 1, respectivamente.
    
    Uma camada Flatten para transformar a saída das camadas convolucionais em um vetor.
    Uma camada Dense com 512 unidades e função de ativação ReLU.
    Uma camada Dense com o número de unidades igual ao número de ações disponíveis no ambiente
    e função de ativação linear.
    
    A entrada do modelo é uma observação do ambiente (uma imagem) e a saída é um vetor de valores
    Q que representam a qualidade de cada ação possível no estado atual do ambiente.
    """
    #Define o formato de entrada da rede neural baseado na forma do espaço de observação do ambiente(uma imagem)
    input_shape = ambiente.observation_space.shape
    #Define o número de ações possíveis que o agente pode tomar, baseado no espaço de ações do ambiente
    número_de_ações = ambiente.action_space.n
    
    # Cria um modelo sequencial utilizando camadas convolucionais e totalmente conectadas.
    modelo = Sequential([
        # Adiciona uma camada de convolução 2D com 32 filtros, um kernel de 8x8, um stride de 4 e função de ativação ReLU
        Conv2D(32, 8, strides=4, activation='relu', input_shape=input_shape),        
        # Adiciona outra camada de convolução 2D com 64 filtros, um kernel de 4x4, um stride de 2 e função de ativação ReLU
        Conv2D(64, 4, strides=2, activation='relu'),       
        # Adiciona uma terceira camada de convolução 2D com 64 filtros, um kernel de 3x3, um stride de 1 e função de ativação ReLU
        Conv2D(64, 3, strides=1, activation='relu'),       
        # Adiciona uma camada Flatten que transforma o tensor de saída das camadas convolucionais em um vetor unidimensional
        Flatten(),      
        # Adiciona uma camada Dense (totalmente conectada) com 512 unidades e função de ativação ReLU
        Dense(512, activation='relu'),       
        # Adiciona uma camada Dense com um número de unidades igual ao número de ações possíveis e função de ativação linear
        Dense(número_de_ações, activation='linear')
    ])
    
    # Retorna o modelo criado
    return modelo
