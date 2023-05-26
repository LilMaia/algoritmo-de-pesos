import tensorflow
import numpy as np
from tensorflow.keras import initializers
from tensorflow.keras.layers import Dense

def gerar_ação(observação, modelo, pesos_do_membro, atualizar_pesos):
    tensorflow.keras.utils.disable_interactive_logging()
    
    # Ajusta a observação para ter a dimensão esperada pelo modelo
    observação = np.expand_dims(observação, axis=0)
    
    if(atualizar_pesos == True):
        # Acessa os pesos das camadas densas do modelo
        shapes_pesos_camadas_densas = [peso.shape for layer in modelo.layers if isinstance(layer, Dense) for peso in layer.get_weights()]
        pesos_organizados = []
        indice_peso = 0

        for shape in shapes_pesos_camadas_densas:
            tamanho_peso = np.prod(shape)
            pesos_peso = np.array(pesos_do_membro[indice_peso:indice_peso + tamanho_peso]).reshape(shape)
            pesos_organizados.append(pesos_peso)
            indice_peso += tamanho_peso
        
        # Acessa as camadas densas do modelo
        camadas_densas = [layer for layer in modelo.layers if isinstance(layer, Dense)]
        
        # Define os pesos das camadas densas
        i = 0
        for camada_densa in camadas_densas:
            camada_densa.set_weights([pesos_organizados[i], pesos_organizados[i+1]])
            i += 2
        
        print(f"Pesos atualizados !!!")
    
    # Realiza a predição utilizando o modelo atualizado com os pesos do membro
    melhores_ações = modelo.predict(observação)

    # Define um limiar (threshold) para converter as probabilidades em 0s e 1s
    limiar = 0.5

    # Converte as probabilidades em 0s e 1s usando o limiar
    ações_binárias = [1 if p > limiar else 0 for p in melhores_ações[0]]

    # Converte a lista em um array numpy
    ações_binárias = np.array(ações_binárias)

    return ações_binárias

def criar_pesos_iniciais(tamanho_da_população, modelo):
    
    # Define a quantidade de pesos que cada indivíduo terá
    quantidade_de_pesos = sum(layer.count_params() for layer in modelo.layers if isinstance(layer, Dense))
    print(f"Criando pesos iniciais : {quantidade_de_pesos}")
    initializer = initializers.HeUniform()
    população = initializer((tamanho_da_população, quantidade_de_pesos))
    
    return população
