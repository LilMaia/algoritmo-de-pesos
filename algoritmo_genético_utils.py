import numpy as np

def selecionar_elites(pesos_da_população, lista_de_aptidão, tamanho_da_população):
    
    # Seleciona os índices dos membros mais aptos (40% do vetor)
    elite_índice = np.argsort(lista_de_aptidão)[::-1][:int(tamanho_da_população*0.4)]
    print(f"Elite indices: {elite_índice}")
    
    # Obtém os pesos dos membros mais aptos
    elite_pesos = np.take(pesos_da_população, elite_índice, axis=0)
    
    return elite_pesos