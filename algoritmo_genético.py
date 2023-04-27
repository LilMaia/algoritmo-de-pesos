import numpy as np

def gerar_nova_população(elite_pesos, taxa_de_mutação, taxa_de_cruzamento, tamanho_da_população):
    print(f"---------------------------------------------------------------------------")
    print(f"Algoritmo genético:")
    # Converte a lista de arrays em um array bidimensional
    elite_pesos = np.vstack(elite_pesos)

    # Inicia a lista que armazenará os novos pesos
    novos_pesos = []

    # Realiza cruzamento entre pares de pesos selecionados aleatoriamente da elite
    for i in range(int(taxa_de_cruzamento * len(elite_pesos) * tamanho_da_população)):
        pai1, pai2 = np.random.choice(len(elite_pesos), 2, replace=False)
        filho = np.concatenate((elite_pesos[pai1][:len(elite_pesos[pai1])//2], elite_pesos[pai2][len(elite_pesos[pai2])//2:]))
        novos_pesos.append(filho)

    # Realiza mutação em cada novo indivíduo gerado pela etapa anterior
    for i in range(len(novos_pesos)):
        if np.random.rand() < taxa_de_mutação:
            novos_pesos[i] += np.random.normal(0, 0.1, size=novos_pesos[i].shape)

    # Retorna a nova lista de pesos com tamanho definido pela população
    novos_pesos = novos_pesos[:tamanho_da_população]
    novos_pesos = np.vstack(novos_pesos)

    print(f"Novos pesos: {novos_pesos}")
    print(f"---------------------------------------------------------------------------")
    return novos_pesos
