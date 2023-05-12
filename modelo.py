from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D

def criar_modelo(ambiente):
    input_shape = ambiente.observation_space.shape
    número_de_ações = 12
    
    # Cria um modelo sequencial utilizando camadas convolucionais e totalmente conectadas.
    modelo = Sequential([
            Conv2D(32, 3, strides=1, activation='relu', input_shape=input_shape),
            Conv2D(32, 3, strides=1, activation='relu'),
            MaxPooling2D(pool_size=(2, 2)),
            Conv2D(64, 3, strides=1, activation='relu'),
            Conv2D(64, 3, strides=1, activation='relu'),
            MaxPooling2D(pool_size=(2, 2)),
            Conv2D(128, 3, strides=1, activation='relu'),
            Conv2D(128, 3, strides=1, activation='relu'),
            MaxPooling2D(pool_size=(2, 2)),
            Conv2D(256, 3, strides=1, activation='relu'),
            Conv2D(256, 3, strides=1, activation='relu'),
            MaxPooling2D(pool_size=(2, 2)),
            Conv2D(512, 3, strides=1, activation='relu'),
            Conv2D(512, 3, strides=1, activation='relu'),
            MaxPooling2D(pool_size=(2, 2)),
            Flatten(),
            Dense(2048, activation='relu'),
            Dense(1024, activation='relu'),
            Dense(número_de_ações, activation='sigmoid')
        ])
        
    # Retorna o modelo criado
    return modelo