from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model

def criar_modelo(ambiente):
    input_shape = ambiente.observation_space.shape
    número_de_ações = 12

    # Carrega a rede Inception pré-treinada sem a camada de saída
    base_model = InceptionV3(weights='imagenet', include_top=False, input_shape=input_shape)

    # Define o atributo trainable das camadas convolucionais da rede Inception como False
    for layer in base_model.layers:
        if not isinstance(layer, Dense):
            layer.trainable = False


    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.25)(x)
    x = Dense(512, activation='relu')(x)
    x = Dropout(0.5)(x)
    predictions = Dense(número_de_ações, activation='sigmoid')(x)

    # Cria o modelo final
    modelo = Model(inputs=base_model.input, outputs=predictions)

    return modelo