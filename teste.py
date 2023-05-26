import numpy as np

from armazenamento import carregar_população
from população_utils import avaliar_aptidão

def testar_geração(ambiente, nome_do_arquivo, modelo):
    pesos_da_população = carregar_população(nome_do_arquivo)
    try:
        lista_de_aptidão = avaliar_aptidão(ambiente, pesos_da_população, modelo)
    except KeyboardInterrupt:
        return
    aptidão_máxima = np.max(lista_de_aptidão)
    print(f'Aptidão Máxima = {aptidão_máxima}')