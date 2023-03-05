import numpy as np

# função para salvar a população atual
def save_population(population, filename):
    with open(filename, 'wb') as f:
        np.savez(filename, *population)

# função para carregar a população de um arquivo
def load_population(filename):
    with np.load(filename) as data:
        population = [data[f] for f in data.files]
    return population
