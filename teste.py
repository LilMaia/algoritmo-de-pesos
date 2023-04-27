import numpy as np

from armazenamento import carregar_população
from população_utils import avaliar_aptidão

def testar_geração(ambiente, nome_do_arquivo, modelo):
    """
    Este código define a função testar_geração, que carrega
    uma população de pesos para um modelo de rede neural
    de um arquivo específico (com o nome fornecido como entrada para a função),
    executa essa população no ambiente de aprendizado por reforço fornecido como
    entrada e imprime a aptidão máxima alcançada pelos membros
    dessa população durante a avaliação.
    """
    pesos_da_população = carregar_população(nome_do_arquivo)
    try:
        lista_de_aptidão = avaliar_aptidão(ambiente, pesos_da_população, modelo)
    except KeyboardInterrupt:
        return
    aptidão_máxima = np.max(lista_de_aptidão)
    print(f'Aptidão Máxima = {aptidão_máxima}')