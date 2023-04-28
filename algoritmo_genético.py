import numpy as np

def gerar_nova_população(elite_pesos, taxa_de_mutação, taxa_de_cruzamento, tamanho_da_população):
    print(f"---------------------------------------------------------------------------")
    print(f"Algoritmo genético:")
    # Converte a lista de arrays em um array bidimensional
    elite_pesos = np.vstack(elite_pesos)
    print(f"Elite pesos: {elite_pesos}")

    # Inicia a lista que armazenará os novos pesos
    novos_pesos = []

    # Realiza cruzamento entre pares de pesos selecionados aleatoriamente da elite e/ou indivíduos aleatórios
    for i in range(tamanho_da_população):
        if np.random.rand() < taxa_de_cruzamento or len(novos_pesos) == 0:
            # Escolhe dois pais aleatórios da elite e realiza recombinação uniforme para gerar um filho
            pai1, pai2 = np.random.choice(len(elite_pesos), 2, replace=False)
            indices = np.random.choice([0, 1], size=elite_pesos[pai1].shape[0])
            novo_indivíduo = np.where(indices, elite_pesos[pai1], elite_pesos[pai2])
        else:
            # Escolhe um indivíduo aleatório da elite ou gera um novo aleatório
            escolhido = np.random.randint(len(elite_pesos))
            novo_indivíduo = elite_pesos[escolhido] + np.random.normal(0, 0.1, size=elite_pesos[escolhido].shape)

        novos_pesos.append(novo_indivíduo)

    # Realiza mutação em cada novo indivíduo gerado pela etapa anterior
    for i in range(len(novos_pesos)):
        if np.random.rand() < taxa_de_mutação:
            novos_pesos[i] += np.random.normal(0, 0.1, size=novos_pesos[i].shape)

    # Retorna a nova lista de pesos com tamanho definido pela população
    novos_pesos = np.vstack(novos_pesos)

    print(f"Novos pesos: {novos_pesos}")
    print(f"---------------------------------------------------------------------------")
    return novos_pesos[:tamanho_da_população]

