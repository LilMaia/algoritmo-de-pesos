import numpy as np

# função para salvar a população atual
def salvar_população(população, nome_do_arquivo):
    with open(nome_do_arquivo, 'wb') as f:
        np.savez(nome_do_arquivo, *população)

# função para carregar a população de um arquivo
def carregar_população(nome_do_arquivo):
    with np.load(nome_do_arquivo) as data:
        população = [data[f] for f in data.files]
        população = np.vstack(população)
    return população
