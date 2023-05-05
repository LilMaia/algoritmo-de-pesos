from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, Dropout

def criar_modelo(ambiente):
    input_shape = ambiente.observation_space.shape
    número_de_ações = ambiente.action_space.n
    
    # Cria um modelo sequencial utilizando camadas convolucionais e totalmente conectadas.
    modelo = Sequential([
            Conv2D(32, 8, strides=4, activation='relu', input_shape=input_shape),
            Conv2D(64, 4, strides=2, activation='relu'),
            Conv2D(64, 3, strides=1, activation='relu'),
            Conv2D(128, 3, strides=1, activation='relu'),
            Flatten(),      
            Dense(512, activation='relu'),
            Dense(256, activation='relu'),
            Dense(número_de_ações, activation='linear')
        ])
        
    # Retorna o modelo criado
    return modelo