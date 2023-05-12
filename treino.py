import numpy as np
from armazenamento import salvar_população, carregar_população
from algoritmo_genético import gerar_nova_população
from algoritmo_genético_utils import selecionar_elites
from plotagem import plota_pontuação
from modelo_utils import criar_pesos_iniciais
from população_utils import avaliar_aptidão

def treino(ambiente, nome_do_arquivo, tamanho_da_população, número_de_gerações, taxa_de_mutação, modelo):
    # Inicia as listas para armazenar as pontuações máximas e médias de cada geração
    pontuações_máximas = []
    média_das_pontuações = []
    
    try:
        # Tenta carregar a população do arquivo
        pesos_da_população = carregar_população(nome_do_arquivo)
        print(f"População carregada de {nome_do_arquivo}")
    except FileNotFoundError:
        # Se o arquivo não existe, cria uma nova população
        pesos_da_população = criar_pesos_iniciais(tamanho_da_população, modelo)
        print(f"Arquivo {nome_do_arquivo} não encontrado. Iniciando uma nova população.")

    # Loop pelas gerações
    for i_geração in range(número_de_gerações):
        print(f"-------------------------------------------------------------------------------------")
        print(f"treino:")
        print(f"Começando a geração {i_geração}")
        print(f"-------------------------------------------------------------------------------------")
        try:
            # Avalia o fitness de cada indivíduo na população
            lista_de_aptidão = avaliar_aptidão(ambiente, pesos_da_população, modelo)
            # Seleciona os indivíduos mais aptos
            elite_pesos = selecionar_elites(pesos_da_população, lista_de_aptidão, tamanho_da_população)
            # Gera uma nova população a partir dos indivíduos selecionados
            novos_pesos = gerar_nova_população(elite_pesos, taxa_de_mutação, tamanho_da_população)
            # Substitui a população anterior pela nova população
            pesos_da_população = novos_pesos

            # Calcula e armazena as pontuações máxima e média da geração
            aptidão_máxima = np.max(lista_de_aptidão)
            média_de_aptidão = np.mean(lista_de_aptidão)
            pontuações_máximas.append(aptidão_máxima)
            média_das_pontuações.append(média_de_aptidão)

            # Imprime a pontuação máxima da geração atual
            print(f'Geração {i_geração}: Max Fitness = {aptidão_máxima} e Pontuação Média =  {média_das_pontuações}')

            # Salva a população atual no arquivo
            salvar_população(pesos_da_população, nome_do_arquivo)
            print(f"População salva em {nome_do_arquivo} na geração {i_geração}.")

        except KeyboardInterrupt:
            # Se o usuário interromper a execução, salva a população atual no arquivo
            salvar_população(pesos_da_população, nome_do_arquivo)
            print(f"População salva em {nome_do_arquivo} na geração {i_geração}.")
            break

    # Plota as pontuações máximas e médias de cada geração
    plota_pontuação(pontuações_máximas, média_das_pontuações)