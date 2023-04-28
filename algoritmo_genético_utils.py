import numpy as np

def selecionar_elites(pesos_da_população, lista_de_aptidão, tamanho_da_população):
    """
    Seleciona os membros mais aptos da população, com base na lista de pontuação.
    Retorna os pesos dos membros mais aptos.
    """
    print(f"-------------------------------------------------------------------------------------")
    print(f"algoritmo_genético_utils:")
    
    # Seleciona os índices dos membros mais aptos (metade do vetor)
    elite_índice = np.argsort(lista_de_aptidão)[::-1][:int(tamanho_da_população/2)]
    print(f"Elite indices: {elite_índice}")
    
    # Obtém os pesos dos membros mais aptos
    elite_pesos = pesos_da_população[elite_índice.astype(int)]
    
    # Retorna os pesos dos membros mais aptos
    print(f"-------------------------------------------------------------------------------------")
    return elite_pesos
